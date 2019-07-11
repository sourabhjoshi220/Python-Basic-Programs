x=int(input("Enter the number:"))
for i in range (x+1):
    num=i
    result=0
    n=len(str(i))

while(i!=0):
    digit=i%10
    result=result+digit**n
    i=i//10
    if (num==result):
        print(num,"is Armstrong Number")
    else:
        print(num,"Not a armstrong number")
        break
