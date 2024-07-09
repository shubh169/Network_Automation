from paramiko import client, ssh_exception
import sys
import traceback
import socket
import paramiko.util
import datetime

# Log file.
paramiko.util.log_to_file("paramiko.log", level="DEBUG")

user_name = "root"
password = "landisRoot"
# linux_commands = ["cd /opt/iprf/firmware && ./ask_node","ifconfig"]
with open('command.txt') as command_data:
    new_command=command_data.readlines()

def device_manager(hostname, linux_command):
    try:
        print(f"connecting to the device {hostname}.")
        now=datetime.datetime.now().replace(microsecond=0)
        current_config_file = f"{now.strftime('%Y-%m-%d_%H-%M-%S')}_{hostname}.txt"
        ssh_client = client.SSHClient()
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
        with open(current_config_file,'w') as cmd_data:
            for cmd in linux_command:
                print(f"\n {'*' * 20} Executing {cmd} {'*' * 20} ")
                stdin, stdout, stderr = ssh_client.exec_command(cmd)
                output=stdout.read().decode()
                cmd_data.write(output)
                error = stderr.read().decode()
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


device_manager("10.91.77.131", new_command)


