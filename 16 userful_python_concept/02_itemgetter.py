from operator import itemgetter

interface_list = [
    {'name': 'Gi1',
     'ip': '192.168.1.1',
     'mask': '255.255.255.0'},
    {'name': 'Gi2',
     'ip': '192.168.1.2',
     'mask': '255.255.255.0'},
    {'name': 'Gi3',
     'ip': '192.168.1.3',
     'mask': '255.255.255.0'},
    {'name': 'Gi4',
     'ip': '192.168.1.0',
     'mask': '255.255.255.0'},
]

# dict_getter=itemgetter('ip','name','mask')
# # print(dict_getter)
# # print(dict_getter(interface_list[2]))
#
# ip_list,name_list,mask_list=[],[],[]
#
# for interface in interface_list:
#     i=dict_getter(interface)
#     ip_list.append(i[0])
#     name_list.append(i[1])
#     mask_list.append(i[2])
# #
# print(ip_list,name_list,mask_list)
#
# print(f"device ip:{i[0]}")
# print(f"device name:{i[1]}")
# print(f"device mask:{i[2]}")

# vendors = ['cisco', 'arista', 'juniper', 'cumulus', 'extreme']
# list_getter = itemgetter(2)
# # print(list_getter(vendors))
#
# for vendor in vendors:
#     print(list_getter(vendor))
