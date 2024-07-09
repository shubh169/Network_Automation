import re

# str='''DC01 IND R1'''
# print(re.search(pattern=r".+1$", string=str))
# print(re.findall(pattern=r".+1$", string=str))
# r=re.finditer(pattern=r".+1$", string=str)
# for i in r:
#     print(i.group())

# if data in multiline.

# str="""DC01 IND R1
# DC02 IND R1
# DC03 IND R1"""
#
# print(re.search(pattern=r".+1$", string=str, flags=re.MULTILINE))
# print(re.findall(pattern=r".+1$", string=str, flags=re.MULTILINE))
# r=re.finditer(pattern=r".+1$", string=str, flags=re.MULTILINE)
# for data in r:
#     print(data.group())

# print(re.search(pattern=r"^D.+1\Z", string=str, flags=re.MULTILINE))
# print(re.findall(pattern=r"^D.+1\Z", string=str, flags=re.MULTILINE))
# r=re.finditer(pattern=r"^D.+1\Z", string=str, flags=re.MULTILINE)
# for data in r:
#     print(data.group())


'''
\b:Matches the empty string,
 but only at the beginning or end of a word. 

 \B
Matches the empty string, 
but only when it is not at the beginning or end of a word. 
 '''
# matches empty string only at beginning or end
# my_pattern = re.compile(r'\Bcisco')
# string1 = 'fgciscoroutercisco'
# print(my_pattern.search(string1))
############################################
'''{m,n}'''
# my_pattern = re.compile(r'cisco{2,5}')
# string1 = 'ciscorouterciscoooo'
# print(my_pattern.search(string1))
############################################
''' \''''
# noinspection PyRedeclaration
# my_pattern = re.compile(r'\*\n')
# print(my_pattern.search(ver_output))
############################################

'''IGNORECASE'''
# print(re.search('hello', 'Hello', re.I))
############################################
'''DOTALL
by default, dot matches any character except the newline'''

# print(re.search('hello.hello', 'Hello\nHello', flags= re.DOTALL | re.IGNORECASE))
# print(re.search('hello.hello', 'Hello\nHello'))

############################################
'''match'''
my_string = 'abcd1234abcd'
# print(re.match('abcd', my_string)) # None
# print(re.search('1234abcd', my_string)) # match:
print(re.fullmatch('abcd1234abcd', my_string)) # match

############################################
'''sub'''
# noinspection PyRedeclaration
my_string = 'VLAN100 ip address 1.1.1.1 VLAN200, VLAN300'
# print(re.sub(r'V', r'Vx', my_string))
print(re.subn(r'V', r'Vx', my_string))

