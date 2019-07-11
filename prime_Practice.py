num=int(input("Enter the number:"))

if num > 1:
    for i in range(2, num):
        if(num%i==0):
            print(num,"Number is not prime")
            print(i,"time",num%i,"is",num)
            break
        else:
            print(num,"number is Prime Number")
            break

else:
    print("Number is not prime number")
    
