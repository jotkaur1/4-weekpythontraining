class sum:
    def s(self,a,b):
        print("sum=",a+b)

obj= sum()
print("enter two numbers for sum:")
a= int(input())
b=int(input())
obj.s(a,b)
#########constructor###########
print()
class a:
    x=30
    y=5
    def __init__(self):
        print("constructor called")
        print(self.x+self.y)
    def f(self,a,b):
        print("class function called")
        print(a+b)
    def __del__(self):
        print("destructor called")
    def __str__(self):
        print("string fuction called")
p=23
q=15
ob=a()
ob.f(p,q)

del ob
print(ob)
