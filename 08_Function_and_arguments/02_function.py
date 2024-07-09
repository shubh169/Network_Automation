import string
import random


def user_cmd_get(user,priv):
    password="".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))
    return f"username {user} privilege {priv} secret password :{password}\n"

# with open('test.txt','w') as file:
#     file.write(user_cmd_get('admin1',6))
#     file.write(user_cmd_get('admin2', 8))
#     file.write(user_cmd_get('admin1', 9))

# Keyword argument.
# print(user_cmd_get(user="shubham",priv=34))


# List argument.
u_list=["admin2",13]
# print(user_cmd_get(u_list[0],u_list[1]))
# print(user_cmd_get(*(u_list)))
# print(user_cmd_get(*(['admin4',45])))

# Dict argument.
# u_dict={'user':'admin5','priv':100}
#
# print(user_cmd_get(**(u_dict)))