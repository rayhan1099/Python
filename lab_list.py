
fruits=["apple","banana","orange"]
print(fruits)
for x in (fruits):
    print(x)
str="      Hello world     "
print(str.strip(" "))
print(len(str))
print(fruits.index("apple"))
fruits.insert(2,"mango")
print(fruits)
del fruits[1]
print(fruits)
list=[5,6,7,8,9,2,1,2]
s=list.count(2)
print(s)
lst=['A','B','C','D','A']
print(lst.count('A'))
lst.reverse()
print(lst)
carlist=['ford','mistubishe','bmw','vw']
r=[]
for x in (carlist):
    r.append(len(x))
print(r)
print(sum(r))
