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
