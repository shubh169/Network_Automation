import string
import random


def user_cmd_get(user,priv,*args,**kwargs):
    password="".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))
    print(f"username {user} privilege {priv} secret password :{password}\n")
    print("commands are:")
    for cmd in args:
        print(cmd)

    for data in kwargs:
        print(kwargs[data])

lst=["status","ifconfig","pwd"]
user_dict={'place':'noida','pass':1234}
print(user_cmd_get("admin2",20,*lst,**user_dict))