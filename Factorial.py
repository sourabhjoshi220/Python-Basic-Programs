def fact(num):
    if num == 1:
        return num
    else:
        return num*fact(num-1)

num=int(input("Enter the Number"))

if num<0:
    print("Number is notr valid")
elif num==0:
     print("factorial of 0 is 1")
else:
    print("Factorial is: ",fact(num))
    
