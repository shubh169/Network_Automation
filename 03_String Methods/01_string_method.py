username="landisroot123"
print(dir(username))
print(username.upper())
print(username.lower())
print(username.capitalize())
print(username.casefold())

user_input=input("Enter username:").casefold().strip().replace(' ','')
if user_input==username:
    print(f"username {user_input} matched.")
else:
    print("not matched.")

