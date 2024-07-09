# With the help of this script we are run multiple commands on multiple collectors.

import csv
import time
import paramiko
import sys


conf_dict = {'10.91.77.219': ['pwd',
                              'ifconfig',
                              'status'
                             ],
             '10.91.77.161': ['pwd',
                              'ifconfig',
                              'status'],
             '10.91.77.131': ['pwd',
                              'ifconfig',
                              'status']
             }



# for ip, conf_cmd in conf_dict.items():
#     print(f"Connecting to the device: {ip}")
#     for cmd in conf_cmd:
#         time.sleep(.5)
#         print(cmd)

session = paramiko.client.SSHClient()
session.load_system_host_keys()
session.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
for ip, conf_cmd in conf_dict.items():
    try:
        print(f"\n{'#' * 50}\nConnecting to the Device {ip}\n{'#' * 50} ")
        session.connect(hostname=ip,
                        username='root',
                        password='landisRoot',
                        look_for_keys=False,
                        allow_agent=False
                        )
        device_access = session.invoke_shell()
        print(f"\nExecuting Commands are\n{'~' * 22}")
        for conf in conf_cmd:
            device_access.send(conf + '\n')
            time.sleep(.5)
            output = device_access.recv(65000)
            print(output.decode('ascii'), end='')
            time.sleep(10)
        session.close()
    except:
        print('Can not connect to the device')

print(f"\n{'#' * 50}\nCOMMAND EXECUTION COMPLETED\n{'#' * 50}\n")
