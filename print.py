x=12345
y="abcde"
i=0
while x>0:
    r=x%10
    x=x//10
    print("%s%s,"%(r,y[i]),end="")
    i+=1
    
