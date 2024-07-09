from password_generator import generate_password

users=['user1','user2','user3']

final_user_list=[]

for user in users:
    user_dict = {}
    user_dict['username'] = user
    user_dict['password']=generate_password()
    final_user_list.append(user_dict)

print(final_user_list)