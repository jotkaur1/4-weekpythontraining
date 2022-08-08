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





