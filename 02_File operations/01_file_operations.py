import os
#
# Current directory.
# print(os.getcwd())
# Change the directory.
# os.chdir("../Paramiko")
# print(os.getcwd())
#
# total number of file in current dir.
# print(os.listdir())
# print(len(os.listdir()))
# print(f"Current working directory: {os.getcwd()}")
# print(os.system('ls -l'))
#
# How to use loop in file system.
# files=os.listdir()
# files.sort()
# for file in files:
#     print(file)
#     with open (file) as file_data:
#         if "ssh" in file.casefold():
#             print(f"{'#'*20} {file} {'#'*20}")
#         print(type(file_data))
#             print(file_data.read())
#
#
# file1=open('config.txt')
# print(file1.read())
# print(file1.readline())
# print(file1.readline())
# print(file1.readline())
# print(file1.readline())
# commands=file1.readlines()
# for command in commands:
#     print(command.rstrip('\n'))
# file1.close()
""" with open """
# with open("config.txt") as file1:
#     commands=file1.readlines()
#
# for command in commands:
#     print(command.rstrip('\n'))

"""write a file """
# with open('config2.txt','w') as file1:
#     file1.write('testdata1\ntestdata2\ntestdata3\ntestdata4\n')

with open('test_file.pdf', 'rb') as source_file:
    s=source_file.read()

with open('new_file.pdf','wb') as destination_file:
    destination_file.write(s)

# remove file.
os.remove('test.txt')
