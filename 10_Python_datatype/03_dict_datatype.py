dict={
    'ip':'192.168.127.12',
    'user':'admin',
    'password':'shubh911',
    'os':'linux',
    'place':'USA',
    'device_type':'cisco_ios'
}

# Dict are mutable.
# dict['new_ip']='192.168.127.11'
# print(dict)
# dict['new_ip']='192.168.127.18'
# print(dict)
# print(dict.get('ip'))
#
# dict.setdefault('place','india')
# print(dict)

key=['a','b','c','d']
values=['linux','window','linux','window']
new_dict=dict.fromkeys(key,values)
print(new_dict)