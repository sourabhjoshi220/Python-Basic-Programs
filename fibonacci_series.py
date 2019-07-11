n=int(input("Enter the number:"))

x=0
y=1

for i in range(n+1):
    print(x)
    temp=x
    x=y
    y=temp+y

    print(y)
    
    
