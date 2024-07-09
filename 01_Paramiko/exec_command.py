from paramiko import client

user_name="root"
password="landisRoot"
linux_commands=["ifconfig","pwd"]

def device_manager(hostname,linux_commands):
    print(f"connecting to the device {hostname}.")
    ssh_client=client.SSHClient()
    ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
    ssh_client.connect(
        hostname=hostname,
        port=22,
        username=user_name,
        password=password,
        look_for_keys=False,
        allow_agent=False
    )
    print("Connected to remote host.")



    for cmd in linux_commands:
        print(f"\n {'*'*20} Executing {cmd} {'*'*20} ")
        stdin,stdout,stderr=ssh_client.exec_command(cmd)
        print(stdout.read().decode())
        error=stderr.read().decode()
        if error:
            print(f"Error occured: {error}")

# Connect multiple collector.
device_manager("10.91.77.152",linux_commands)
# device_manager("10.91.77.131",linux_commands)

