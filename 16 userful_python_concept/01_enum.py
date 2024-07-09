# from pprint import pprint
# vendors=["cisco","arista","juniper","cumulus","extreme"]
#
# for data in enumerate(vendors,start=1):
#     pprint(data)

users=["shubham","admin","nikhil","apoo"]
search=input("enter user:").casefold()
for index,name in enumerate(users):
    if name==search:
        print(f"User {search} fonud on indrx number {index}")
        break
else:
    print("User not found")