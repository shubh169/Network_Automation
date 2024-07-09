import paramiko
import socket
import datetime


class SSHManager:
    def __init__(self, hostname, username, password, commands_file='command.txt'):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.commands_file = commands_file

    def connect(self):
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(
                hostname=self.hostname,
                port=22,
                username=self.username,
                password=self.password,
                look_for_keys=False,
                allow_agent=False
            )
            print("Connected to remote host.")

        except (socket.gaierror, paramiko.AuthenticationException) as e:
            print(f"Connection error: {e}")

    def execute_commands(self):
        try:
            with open(self.commands_file) as commands_data:
                commands = commands_data.readlines()

            timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            output_filename = f"{timestamp}_{self.hostname}.txt"

            with open(output_filename, 'w') as output_file:
                for cmd in commands:
                    print(f"\n {'*' * 20} Executing {cmd.strip()} {'*' * 20} ")
                    stdin, stdout, stderr = self.ssh_client.exec_command(cmd.strip())
                    output = stdout.read().decode()
                    output_file.write(output)
                    error = stderr.read().decode()
                    if error:
                        print(f"Error occurred: {error}")
        except Exception as e:
            print(f"Execution error: {e}")

    def disconnect(self):
        if hasattr(self, 'ssh_client'):
            self.ssh_client.close()
            print("Disconnected from remote host.")
        else:
            print("Not connected to any host.")


ssh_manager = SSHManager(hostname="10.91.77.131", username="root", password="landisRoot")
ssh_manager.connect()
ssh_manager.execute_commands()
ssh_manager.disconnect()
