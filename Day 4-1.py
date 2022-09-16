n=int(input("enter a number:"))
a=[]
for i in range(1,n+1):
    if(i%3==0):
        if(i%5==0):
            b="fizzbuzz"
            a.append(b)
        else:
            b="fizz"
            a.append(b)
    elif(i%5==0):
        b="buzz"
        a.append(b)
    else:
        a.append(i)
print(a)
