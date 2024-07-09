# Sorting list based on number on elements in word.

# my_list=["abcd",'shu','ab','cd']
#
# def length_cals(l):
#     return len(l)
#
#
# my_list.sort(key=length_cals)
# print(my_list)



list3 = [
    {'id': 1,
     'user': 'admin3',
     'password': 'pwd1'
     },
    {'id': 3,
     'user': 'admin1',
     'password': 'pwd1'
     },
    {'id': 2,
     'user': 'admin2',
     'password': 'pwd1'
     },
    {'id': 5,
     'user': 'admin1',
     'password': 'pwd1'
     }
]

def sort_logic(d):
    return d['id']

list3.sort(key=sort_logic, reverse=True)
print(list3)