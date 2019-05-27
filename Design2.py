for i in range(5):
    for j in range(5):
        if j==0:
            print("*",end="")
        elif j==i:
            print("*",end="")
        elif i==4:
            print("*",end="")
        else:
            print(" ",end="")
    print()
