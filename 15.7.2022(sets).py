s=set()
print("enter elements of set\n")
for i in range(6):
    a=input()
    s.add(a)
print(s)
print("element do you want to delete")
d=input()
s.remove(d)
print(s)
print()
print("frozenset:\n")
f=frozenset(s)
print(type(f))

    
