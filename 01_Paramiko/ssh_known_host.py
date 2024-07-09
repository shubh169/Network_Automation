from paramiko import client
from getpass import getpass
import time


commands=["cd /opt/iprf/firmware","./ask_node"]

user_name=input("Enter your username:")
if not user_name:
    user_name="root"
    print(f"username not provided.consider defalut username {user_name}")
password = getpass(f"\U0001F511 Enter Password of the user {user_name}: ") or "landisRoot"


def device_manager(hostname,commands):
    print(f"connecting to the device {hostname}.")
    ssh_client=client.SSHClient()
    ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
    
    # if we have a private key for this host then use it otherwise rsa key(AutoAddPolicy()) will be used by default.
    # ssh_client.load_system_host_keys()
    # if we want to given filepath to the hostkey.
    # ssh_client.load_host_keys(filename='~/.ssh/known_hosts')
    # if we ignore known hosts and connect anyways.
    # ssh_client.set_missing_host_key_policy(client.WarningPolicy)
    
    ssh_client.connect(
        hostname=hostname,
        port=22,
        username=user_name,
        password=password,
        look_for_keys=False,
        allow_agent=False
    
    )
    print("Connected to remote host.")
    device_access = ssh_client.invoke_shell()
    for cmd in commands:
        device_access.send(f"{cmd}\n")
        time.sleep(10)
        output = device_access.recv(65535)
        print(output.decode(),end='')
    ssh_client.close()
    
device_manager("10.91.77.123",commands)
