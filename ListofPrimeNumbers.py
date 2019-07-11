num1 = int(input("Enter the start value number:")) 
num2 = int(input("Enter the end value number:"))

for i in range(num1,num2+1):
    if i>1:
        for r in range(2, i):
            if(i%r==0):
                break
        else:
            print(i)


    
