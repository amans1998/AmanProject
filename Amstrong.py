print("pls enter the value you want to check")
a=int(input())
b=a
c=0
while b>0:
    b=b//10
    c+=1
b=a
s=0
while b>0:
    r=b%10
    b=b//10
    s=s+r**c
if a==s:
    print("given number is an amstrong number")
else:
    print("given number is not a amstrong number")
