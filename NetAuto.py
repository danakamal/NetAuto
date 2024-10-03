import typer
import inquirer
from pythonping import ping
from rich import print as rprint
import napalm 

app = typer.Typer()

@app.command()
def select_option():
    questions = [
        inquirer.List(
        "os",
        message="What Cisco OS are we configuring today?",
        choices=["ios","iosxr","nxos"],
        ),
    ]
    answer = inquirer.prompt(questions)
    os = answer['os']
    #print(os)
    username_pass(os)
    

def username_pass(os):
    questions = [
        inquirer.Text("username", message="Please enter the username?"),
        inquirer.Password("password", message="Please enter the password"),
        inquirer.Text("path", message="Please enter the path to ur file with a list of IP addresses to connect to"),
        ]
    answer = inquirer.prompt(questions)
    user = answer['username']
    password = answer['password']
    path = r"{}".format(answer['path'])
    #print(path)
    ping_ips(path, os, user, password)

def ping_ips(path, os, user, password):
    IPs = open(path, 'r')
    IP_add = []
    for line in IPs:
        ip = line.strip()
        response = ping(ip, count=4)
        status = response.success()
        #print(status)
        if status == True:
            rprint(f"[green]{ip} is reachable[/green]")
            IP_add.append(ip)
        else:
            rprint(f"[red]{ip} is unreachable[/red]")
            break
    if IP_add:       
        bulk_or_not(ip, status, os, user, password, IP_add)

def bulk_or_not(ip, status, os, user, password, IP_add):
    questions = [
        inquirer.Checkbox("type", message="Do you want to config in bulk or individually", choices=["Bulk", "Individual"]),
    ]
    answer = inquirer.prompt(questions)
    types = answer['type']
    
    if 'Bulk' in types:
        questions = [
            inquirer.Text("config", message="Please enter the path to the configuration file"),
        ]
        answer = inquirer.prompt(questions)
        config = r"{}".format(answer['config'])
        
        for ip in IP_add:
            connect_to_device(os, ip, user, password, config)
    else:
        for ip in IP_add:
            questions = [
                inquirer.Text("config", message=f"Please enter the path to the configuration file for {ip}"),
            ]
            answer = inquirer.prompt(questions)
            config = r"{}".format(answer['config'])
            connect_to_device(os, ip, user, password, config)
        

def connect_to_device(os, ip, user, password, config):
    driver = napalm.get_network_driver(os)
    device = driver(hostname=ip, username=user, password=password)
    device.open()
    rprint("[green]Connected to[/green]", ip)
    device.load_merge_candidate(filename=config)
    print(device.compare_config())
    
    questions = [
        inquirer.Checkbox("commit", message=" ", choices=["Commit", "Discard"]),
        ]
    answer = inquirer.prompt(questions)
    commit_status = answer['commit']
    if 'Commit' in commit_status:
        device.commit_config()
        questions = [
            inquirer.Confirm("rollback", message="Do you want to rollback?", default=True),
            ]
        answer = inquirer.prompt(questions)
        rollback = answer['rollback']
        if rollback is True:
            device.rollback()
            print('configuration rolledback ')
        else:
            device.commit_config()
            print('committed')
    else:
        device.discard_config()
        print('Configuration Discarded')

    device.close()

    
if __name__ == "__main__":
    rprint("[red]    )                                       [/red]")
    rprint(r"[red] ( /(           )    (               )      [/red]")
    rprint(r"[red] )\())   (   ( /(    )\       (   ( /(      [/red]")
    rprint(r"[red]((_)\   ))\  )\())((((_)(    ))\  )\()) (   [/red]")
    rprint(r"[red] _((_) /((_)(_))/  )\ _ )\  /((_)(_))/  )\  [/red]")
    rprint(r"[dark_orange]| \| |(_))  | |_   (_)_\(_)(_))( | |_  ((_) [/dark_orange]")
    rprint(r"[dark_orange]| .` |/ -_) |  _|   / _ \  | || ||  _|/ _ \ [/dark_orange]")
    rprint(r"[dark_orange]|_|\_|\___|  \__|  /_/ \_\  \_,_| \__|\___/ [/dark_orange]")
    rprint("                                            ")
    rprint(r"[red]--------------------------------------------------------[/red]")
    rprint(r"[red]--------------------------------------------------------[/red]")
    print("""
The following CLI tool has been developed for automating
network operations on Cisco devices using Python's NAPALM,
through uploading a configuration file. This tool is
intended for learning purposes, and to run on a development
environment. It is recommended to create backups of your
device configurations before running any automation tasks.
By using this tool, you agree that the developers and
contributors are not liable for any damages or issues that
may arise from its use. Use this tool responsibly and in
accordance with your organization's policies and procedures.
""")
    print("Copyright © 2024 Dana Kamal. All rights reserved.")
    rprint(r"[red]--------------------------------------------------------[/red]")
    rprint(r"[red]--------------------------------------------------------[/red]")
    app()
    
