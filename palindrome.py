num=int(input("Enter the number to palindrome:"))

string=str(num)
num_rev= string[::-1]
print("Reversed Number is:",num_rev)
if string==num_rev:
    print("Entered Number is Palindrome")

else:
    print("Number is not Palindrome")
    
