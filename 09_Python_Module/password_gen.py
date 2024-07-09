import string
import random


def user_cmd_get(user,priv):
    password="".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))
    cst_lst= f"username {user} privilege {priv} secret password: {password}\n"
    return cst_lst

lst=[
    {'user':'admin1','priv':20},
    {'user':'admin2','priv':13},
    {'user':'admin3','priv':14}
    ]

def users_cmd_get(*args):
    cmd_list=[]
    for user in args:
        password="".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))
        user_cmd=f"username {user['user']} privilege {user['priv']} secret password :{password}"
        cmd_list.append(user_cmd)
    return cmd_list

if __name__ == '__main__':
    print(user_cmd_get('admin1',20))


