#try,except,finally,else
try:
    print("enter two values")
    a=int(input())
    b=int(input())
    print("division:",a/b)
except TypeError:
    print("typing error.......")
except ZeroDivisorError:
    print("Divison by 0 not allowed")
else:
    print("divison is allowed",a/b)
finally:
    print("finally always executes")

#raise

try:
    x=int(input("enter number upto 1000:"))
    if x>1000:
        raise ValueError(x)
except ValueError:
    print(x,'is not in given range')
else:
    print(x,"is within range of 1000")
