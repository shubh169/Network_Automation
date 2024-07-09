'''   Compile   '''

import re

with open('output.txt') as paramiko_log:
    log_output=paramiko_log.read()

# my_pattern=re.compile(r"(cisco)\.(\w+)")
# result=my_pattern.search(string=log_output)
# print(result)
# print(result.group(0))


'''Compile Example'''

# my_pattern=re.compile(r"C....")
# print(my_pattern.search(string=log_output))
# print(my_pattern.findall(string=log_output))
# results=my_pattern.finditer(string=log_output)
# for result in results:
#     print(result.group())
#     print(result.span())

'''Validate user input'''
#python or python3.10
# user_input=input('Enter python version: ').casefold()
# my_pattern=re.compile(r"^python3$|^python3.10$")
# my_pattern=re.compile(r"python3(\.10)?$")
# result=my_pattern.search(user_input)
# if result:
#     print(f"Matched with {user_input}")
# else:
#     print("Not Matched ")

'''Email validation '''
support_email="please reach out to help@gmail.com, support@gmail.com, admin@gmail.co.in, ab@abc.co.us, abc@aa.co.uk"
email_pattern=re.compile(r"[\w\.-]+@[\w\.-]+.co(m|.)(\w{2})?")
results=email_pattern.finditer(support_email)
for result in results:
    print(result.group())

