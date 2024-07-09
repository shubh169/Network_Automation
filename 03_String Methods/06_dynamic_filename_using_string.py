import datetime

with open('ssh_command.txt') as system_command:
    commands = system_command.readlines()
now=datetime.datetime.now().replace(microsecond=0)

for cmd in enumerate(commands,start=1):
    file_name=f"{str(now).replace(" ","_")}_{str(cmd[0]).zfill(2)}_{cmd[1].strip()}.txt"
    with open(file_name,'w') as system_command:
        system_command.write('test_data')



