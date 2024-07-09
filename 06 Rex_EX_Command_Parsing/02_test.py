# import paramiko
#
# hostname = '10.91.77.131'
# username = 'root'
# password = 'landisRoot'
#
# # Commands to execute sequentially
# commands = [
#     'cd /opt/iprf/profile',
#     'echo "your_config_changes" > config.ini'
# ]
#
# try:
#     ssh_client = paramiko.SSHClient()
#     ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh_client.connect(hostname=hostname, username=username, password=password)
#
#     # Execute commands sequentially
#     for command in commands:
#         stdin, stdout, stderr = ssh_client.exec_command(command)
#         output = stdout.read().decode()
#         error = stderr.read().decode()
#
#         print(f"\n{'*' * 20} Executing: {command} {'*' * 20}")
#         if output:
#             print(output)
#         if error:
#             print(f"Error occurred: {error}")
#
#     ssh_client.close()
#
# except paramiko.SSHException as e:
#     print(f"SSH error: {e}")
# except paramiko.AuthenticationException:
#     print("Authentication failed.")
# except Exception as e:
#     print(f"An error occurred: {e}")

# local_file_path = '/path/to/modified_config.ini'
# remote_file_path = '/opt/iprf/profile/config.ini'
#
# try:
#     ssh_client = paramiko.SSHClient()
#     ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh_client.connect(hostname=hostname, username=username, password=password)
#
#     # Create an SFTP session
#     sftp = ssh_client.open_sftp()
#
#     # Upload the modified config.ini file
#     sftp.put(local_file_path, remote_file_path)
#
#     sftp.close()
#     ssh_client.close()
#
#     print("File uploaded successfully.")
#
# except paramiko.SSHException as e:
#     print(f"SSH error: {e}")
# except paramiko.AuthenticationException:
#     print("Authentication failed.")
# except Exception as e:
#     print(f"An error occurred: {e}")

import re


with open('2024-04-23_11-26-51_10.91.77.131.txt') as ip_data:
    output = ip_data.read()
# Define the regular expression pattern to match IPv6 addresses.
ipv6_pattern = r'[A-Fa-f0-9:]+:[A-Fa-f0-9:]+:[A-Fa-f0-9:]+:[A-Fa-f0-9:]+:[A-Fa-f0-9:]+:[A-Fa-f0-9:]+:[A-Fa-f0-9:]+:[A-Fa-f0-9:]+'

# Find all IPv6 addresses in the digraph string
ipv6_addresses = re.findall(ipv6_pattern, output)

# Print the extracted IPv6 addresses
for address in ipv6_addresses:
    print(address)

ip_address=input("Enter IP Address: ")
print(ip_address)