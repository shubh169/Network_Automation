from paramiko import client,ssh_exception
import sys
import traceback
import socket
import paramiko.util
# Log file.
paramiko.util.log_to_file("paramiko.log", level="DEBUG")

user_name="root"
password="landisRoot"
linux_commands=["cd /opt/iprf/firmware && ./ask_node"]

def device_manager(hostname,linux_commands):
    try:
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
    except socket.gaierror:
        print("Given IP is not valid.")

    except ssh_exception.AuthenticationException:
        print("Authentication Failed, check your credentials.")

    except:
        print("Error occured.")
        print(sys.exc_info())
        # traceback.print_exception(*sys.exc_info())
        


device_manager("10.91.77.123",linux_commands)


