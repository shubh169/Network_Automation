from password_generator import generate_password

users=['user1','user2','user3']

final_user_list=[]

for user in users:
    user_list = []
    user_list.append(user)
    user_list.append(generate_password())
    print(f"id of user_list after every iteration: {id(user_list)}")
    final_user_list.append(user_list)

print(final_user_list)