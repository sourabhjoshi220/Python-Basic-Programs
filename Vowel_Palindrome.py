string=input("Enter the String")
print("String is",string)

vowels=0
consonants=0

for i in string:
    if(i == "A" or i=="a" or i=="E" or i=="e"
       or i=="i" or i=="I" or i=="o" or i=="O"
       or i=="u" or i=="U"):
        vowels=vowels+1
        print("Vowels in String:",i)
    else:
        consonants=consonants+1
        print("Consonants in String:",i)
        
print("No os vowels is:",vowels)
print("no of consonants:",consonants)
 
