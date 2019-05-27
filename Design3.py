a=0
for i in range(5,0,-1):
    for j in range(1,10):
        if i==j:
            print("*",end="")
        elif j==i+a:
            print("*",end="")
        elif i==1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    a+=2
