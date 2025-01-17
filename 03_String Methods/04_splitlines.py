'''splitlines() method is used to split a string into a list of lines.'''

# show_output = '''GigabitEthernet1       192.168.0.63    YES NVRAM  up                    up
# GigabitEthernet2       unassigned      YES NVRAM  up                    up
# GigabitEthernet3       unassigned      YES NVRAM  up                    up
# GigabitEthernet4       unassigned      YES NVRAM  up                    up
# Loopback1001           10.1.1.100      YES manual up                    up
# Loopback1002           20.1.1.100      YES manual up                    up
# '''
# intf_lines=show_output.splitlines()
# for intf in intf_lines:
#     intf_details=intf.split()
#     if intf_details[1]=="unassigned":
#         continue
#     print(f"Interface Name: {intf_details[0]} Device IP: {intf_details[1]}")

with open('output.txt') as data:
    lines = data.readlines()

    print("Press Enter..",end='')
    for line in lines:
        if input()=='':
            line=line.strip('\n')
            print(line,end='')

    print("Completed.")