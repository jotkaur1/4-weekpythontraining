def f():
    global x
    x=20
    print(x)
x=10
f()
##########################################
a=10
def f1():
    print('f1',a)
def g():
    a=20
    print('glo',a)

def h():
    global a
    a=30
    print('h',a)
print('glo',a)
f1()
print('glo',a)
g()
print('glo',a)
h()
print('glo',a)
##########################################
def f1():
    a=37
    print("inside f1()",a)
   
    def f2():
        print("inside f2:")
        nonlocal a
        a=50
        print(a)
    f2()
f1()
###########################################
