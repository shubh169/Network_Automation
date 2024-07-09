import ipaddress

# ip=ipaddress.IPv4Address('192.168.1.1')
# print(type(ip))

# print(ip.version)
# print(ip.max_prefixlen)
# print(ip.reverse_pointer)
# exp=ip.exploded
# print(type(exp))
# print(ip.is_multicast)
# print(ip.is_private)

try:
    ip_address=ipaddress.ip_address(input("Enter IP Address: "))
    print(ip_address)

except ValueError:
    print("Please enter a valid IP Address.")