inventory_dict = {'192.168.0.1': {'name': 'router1',
                                  'username': 'admin1',
                                  'password': 'admin1',
                                  'vendor': 'cisco',
                                  'os': 'ios'},
                  '192.168.0.2': {'name': 'arista2',
                                  'username': 'admin2',
                                  'password': 'admin2',
                                  'vendor': 'arista',
                                  'os': 'eos'},
                  '192.168.0.3': {'name': 'srx3',
                                  'username': 'admin3',
                                  'password': 'admin3',
                                  'vendor': 'juniper',
                                  'os': 'junos'},
                  '192.168.0.4': {'name': 'srx3',
                                  'username': 'admin3',
                                  'password': 'admin3',
                                  'vendor': 'juniper',
                                  'os': 'junos'}
                  }


# print(inventory_dict['192.168.0.1'])
# k=inventory_dict.keys()
# k=inventory_dict.values()
# k = list(inventory_dict.items())
# print(k[0][1]['name'])
#
# for device in inventory_dict.values():
#     print(device['name'])

for ip, details in inventory_dict.items():
    if details['vendor'] == 'juniper':
        print(f"Junifer verdor IP is: {ip}")