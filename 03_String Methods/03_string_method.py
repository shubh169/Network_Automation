""" join() method is used to concatenate elements of an iterable object (such as a list or tuple)
into a single string """

# list=["Cisco","ISO","17.3"]
# print('-'.join(list))


""" ljust() method in Python is used to left-justify a string within a specified width by padding it with a 
specified character on the right side."""

# print("abc".ljust(10), '123456')
# print("abcdef".ljust(10), '123456')
# print("abcdefgh".ljust(10), '123456')
# print("abcxx".ljust(10), '123456')

""""Partition"""
# message="ip route 10.91.77.123"
# print(message.partition("route"))

""" split """
# users="user1,user2,user3,user4,user5"
# users=users.split(",")
# for user in users:
#     print(f"Username is :{user}")

"""splitlines"""
# print("user1\nuser2\nuser3\nuser4".splitlines())

"""z fill"""
# a="abc"
# print(a.zfill(8))

"""translate"""
a="hello world.."
trans={46:33}
print(a.translate(trans))