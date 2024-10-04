# NetAuto
NetAuto is a CLI tool has been developed for automating
network operations on Cisco devices using Python's NAPALM,
through uploading a configuration file. NetAuto provides secure automation through 
the use of SSH and secure copy to transmit configuration files.

This tool is intended for learning purposes, and to run on a development
environment. 

It is recommended to create backups of your
device configurations before running any automation tasks.
By using this tool, you agree that the developers and
contributors are not liable for any damages or issues that
may arise from its use. Use this tool responsibly and in
accordance with your organization's policies and procedures.

```
    )                                 
 ( /(         )   (             )     
 )\())  (  ( /(   )\      (  ( /(
((_)\  ))\ )\()|(((_)(   ))\ )\())(   
_((_)/((_|_))/ )\ _ )\ /((_|_))/ )\
| \| (_)) | |_  (_)_\(_|_))(| |_ ((_) 
| .\`/ -_)|  _|  / _ \ | || |  _/ _ \ 
|_|\_\___| \__| /_/ \_\ \_,_|\__\___/ 
                                      
```
                                          
## Prerequisites
Your system should have Python 3.12 installed, with the following modules to successfully run the tool:
+ pip install inquirer==3.4.0
+ pip install typer==0.12.5
+ pip install rich==1.1.4
+ pip install pythonping==5.0.0
+ pip install napalm==13.9.1

On the networking devices ensure the following is configured:
+ SSH
+ ip scp server enable

## Installation
You can immediately install and run the tool by downloading the NetAuto.py file to your system.

## How to Use
1. From the command line run the tool: _python NetAuto.py_
![1-run](https://github.com/user-attachments/assets/2b8bc761-480a-474d-be5c-01c78aac2f17)

2. Choose the Cisco Operating System, and enter the parameters required for connection. The IP addresses should be added in a .txt file, which is entered in the tool.
![2- IPs and connectivity](https://github.com/user-attachments/assets/9b1decfd-8742-4ae1-904b-991425d774dd)

3. Choose the type of configuration, and then add the path to the configuration file:
   - Bulk: One configuration file for all devices.
   - Individual: Separate configuration files for each device.
![3- config file](https://github.com/user-attachments/assets/4cbeaad9-2aa7-4eb4-90fd-dc17d8bfd581)

4. Finally confirm the changes by either commiting the changes to the devices, or discarding the changes.
![4- confirmation](https://github.com/user-attachments/assets/44cf3e09-c515-4b6c-99c9-33dc2640f053)


