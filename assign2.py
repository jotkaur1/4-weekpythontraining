###########Palindrome
print("enter a string/number:")
s1=input()
l=len(s1)
revs1=s1[::-1]
flag=0
for i in range(l):
        if(s1[i]==revs1[i]):
            i=i+1
        else:
            flag=1
            break
if flag==0:
    print("string/number is palindrome")
else:
    print("sring/number is not palindrome")
#########factorial
print()
def f(n):
    
    fact=1
    if n==0:
        return 1
    else: 
       for i in range(1,n+1):
            fact=fact*i
       return fact
       
print("enter number:")
a=int(input())
print("Factorial is=",f(a))

#############Fibonacci series
print()
def fib(n):
    print("fibonacci series is:")
    a,b=0,1
    
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
    print()
print("enter number:")
x=int(input())
fib(x)
#####validity of a password
l, u, p, d = 0, 0, 0, 0
s = input("enter your password:\n")
if (len(s) >= 8):
    for i in s:

         if (i.islower()):
            l+=1           
         if (i.isupper()):
            u+=1           

         if (i.isdigit()):
            d+=1           
         if(i=='@'or i=='$' or i=='_'):
            p+=1          
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
    print("Valid Password")
else:
    print("Invalid Password")
##########gruoping dictonarary into list
    def gro_dic(l):
       result = {}
       for k, v in l:
         result.setdefault(k, []).append(v)
       return result
colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print("Original list:")
print(colors)
print("\nGrouping a sequence of key-value pairs into a dictionary of lists:")
print(gro_dic(colors))
############covert more than one list into dictionary
print()
def nest(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result

student_id = ["S001", "S002", "S003", "S004"] 
student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
student_grade = [85, 98, 89, 92]
print("Original strings:")
print(student_id)
print(student_name)
print(student_grade)
print("\nNested dictionary:")
ch='a'
print(nest(student_id, student_name, student_grade))
print()
####################subset of a set
print("Check if a set is a subset of another set, using comparison operators and issubset():\n")
x = set(['1','2','3','4','5'])
y = set(['2','3','8'])
z = set(['4'])
print("x: ",x)
print("y: ",y)
print("z: ",z,"\n")
print("If x is subset of y")
print(x <=y)
print(x.issubset(y))
print("If y is subset of x")
print(y <= x)
print(y.issubset(x))
print("\nIf y is subset of z")
print(y <= z)
print(y.issubset(z))
print("If z is subset of y")
print(z <= y)
print(z.issubset(y))
#########################remove empty tuples
print()
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)
#####area program

def area_rec():
    print("enter length and breadth:")
    l=float(input())
    b=float(input())
    area=l*b
    print("area=",area)

def area_cr():
    print("enter radius:")
    l=float(input())
    
    area=3.14*l*l
    print("area=",area)
def area_sq():
    print("enter length of side:")
    l=float(input())
    
    area=l*l
    print("area=",area)
def area_tr():
    print("enter base and height:")
    b=float(input())
    h=float(input())
    area=0.5*b*h
    print("area=",area)

print("1. area of rectangle")
print("2.area of circle")
print("3.area of square")
print("4.area of triagle")

print("enter your choice")
ch=input()
match ch:
    case '1': area_rec()
    case '2': area_cr()
    case '3': area_sq()
    case '4': area_tr()

#### armstrong number
print("enter a number")
num=int(input())
n=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit*n
    temp//=10
if num==sum:
    print(num,"is armstrong number")
else:
    print(num,"is not armstrong number")
print()
####calculator program
print("enter two operands:")
a=int(input())
b=int(input())
print()
print("enter the operator:")
o=input()
match o:
    case '+': print(a+b)
    
    case '-': print(a-b)
    
    case '*': print(a*b)
             
    case '/': print(a/b)
    
    case '%': print(a%b)
    
    case '//': print(a//b)
    
    case '**': print(a**b)
#############pattern program######
 print()
 n=5
for i in range(0,n):
    for j in range(0,i+1):
        print("# ",end="")
    print()
print()
print()

n=5
for i in range(0,n):
    for j in range(0,i+1):
        print(j+1,end="")
    print()
print()
print()

n=5
for i in range(n,0,-1):
    for j in range(0,i):
        print("# ",end="")
    print()
print()
print()

m=5
for i in range(m, 1, -1):
    for space in range(0,m-i):
        print(" ", end="")
    for j in range(i,2*i-1):
        print("* ",end="")

    for j in range(1,i-1):
        print("* ", end="")
    print()

    
####leap year######
print("enter a year")
a=int(input())
if (a%4)==0:
    print("this is leap year")
else:
    print("this is not leap year")
    
######prime number#########
print()

print("enter a number:")
s=int(input())
flag =0
if s>1:
    for i in range(2,s):
        if (s%i)==0:
            flag=1
            break
if flag==1:
    print(s,"is not prime number")
else:
     print(s,"is prime number")
print()
##########reverse a list##########
li=[]
print("enter elements in list:\n")
for x in range(5):
    a=input()
    li.append(a)
print(li)
li.reverse()
print("reverse list",li)
print("max of list:",max(li))
print("min of list:",min(li))


#############sum of list########
print()
def sumlist(li):
    total=0
    for i in li:
        total+=i
    return total

print("sum",sumlist((8,7,6,5,4))






    





