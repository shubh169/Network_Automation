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


