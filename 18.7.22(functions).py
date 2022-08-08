def sumlist(li):
    total=0
    for i in li:
        total+=i
    return total
def mullist(li):
    product=1
    for i in li:
        product*=i
    return product
print("sum",sumlist((8,7,6,5,4)))
print("product",mullist((8,7,6,5,4)))

##########################################################################
print()
def swap(x,y):
    temp=x
    x=y
    y=temp
    print("After swapping: x=",x,"y=",y)

x=5
y=6
print("before swapping: x=",x,"y=",y)
swap(x,y)

############################################################################
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

#############################################################################
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

        
