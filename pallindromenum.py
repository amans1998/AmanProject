print("pls enter the value you want to check")
a=int(input())
b=a
s=0
while b>0:
    r=b%10
    b=b//10
    s=s*10+r
if a==s:
    print("given number is a pallindrome")
else:
    print("given number is not a pallindrome")
