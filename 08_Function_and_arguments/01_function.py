import string
import random


def user_cmd_get(user,priv):
    password="".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))
    return f"username {user} privilege {priv} secret {password}\n"

with open('test.txt','w') as file:
    file.write(user_cmd_get('admin1',6))
    file.write(user_cmd_get('admin2', 8))
    file.write(user_cmd_get('admin1', 9))


