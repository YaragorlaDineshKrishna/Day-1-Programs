a=int(input("enter the numbers:"))
lists=[]
for i in range (0,a):
    b=int(input("enter the number:"))
    lists.append(b)
print(lists)
def sumsquare(lists):
    odd=0
    even=0
    for i in lists:
        if(i%2==0):
            even+=i**2
        else:
            odd+=i**2
    lists=[odd,even]
    return lists
print(sumsquare(lists))
        
