for i in range(5):
    for j in range(9):
        if i==0:
            print("*",end="")
        elif j==i:
            print("*",end="")
        elif j==8-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
