print("welcome")
print("pls enter your name")
c=input()
print("hello "+c)
print("this is a guessing game i would guess a number between 1 to 10")
print("you have three try to geuss what number i have guess")
print("so are you ready")
from random import *
a=randint(1,10)
d=0
e=3
print("try your first guess")
for n in range(3):
    b=int(input())
    if a==b:
        d+=1
        break
    elif n==2:
        print("game over")
        break
    else:
        print("wrong guess")
        e-=1
        print("lives left are "+str(e))
        print("try again")
if d==1:
    print("%s is correct guess" %(b))
else:
    print("Ooo you lost")
    print("the correct answer was "+str(a))
