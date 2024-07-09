# ''' r is used for row string.'''
#
# st=r"\nhello\tthere"
# print(st)
# print(type(st))

import re
with open('output.txt') as paramiko_log:
    log_output=paramiko_log.read()

# my_pattern=r"cisco"
# my_match=re.search(my_pattern,log_output)
# print(my_match)

############################################################################################
# my_pattern=r"Cisco.+, Version (\d\S+)"
# my_match=re.search(my_pattern,log_output)
# ios_version=my_match.group(1)
# print(f"{'IOS_Version:'.ljust(6)} {ios_version}")

############################################################################################

# my_pattern=r"(cisco)\.(com)"
# my_match=re.search(my_pattern,log_output)
# if my_match:
#     print("Match Found")
#     print(my_match.group(0))
#     print(my_match.group(1))
#     print(my_match.group(2))
#
# else:
#     print("No Match")

###########################################################################################
# my_pattern=r"Processor board ID (\d\S+)"
# my_match=re.search(my_pattern,log_output)
# processor_id=my_match.group(1)
#
# print(f"{'Processor Id'.ljust(5)}: {processor_id}")

