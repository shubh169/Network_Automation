# l=[10,20,80,30,20,10,80,30,90,80,30]
# s=set(l)
# print(s)

# s={1,2,3,4,5,6,1,2,3,4}
# s.add(90)
# print(s)
# l=['a','b']
# s.update(l,range(20,30))
# print(s)

# s={1,2,3,4,5}
# s1=s.copy()
# print(s1)
# s.add(100)
# print(s)
# print(s1)
# # s.remove(50)
# s.discard(50)
# print(s)


########Mathematical function on set ############
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.union(s2))
print(s1|s2)
print(s1.intersection(s2))
print(s1&s2)