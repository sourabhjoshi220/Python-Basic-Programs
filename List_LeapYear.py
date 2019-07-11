Year1=int(input("Enter the Starting Year:"))

Year2=int(input("Enter the Ending Year:"))


for year in range(Year1, Year2+1):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                print("{0} year is Leap Year".format(year))
            else:
                print("{0} year is not Leap Year".format(year))
        else:
            print("{0} year is not Leap Year".format(year))
    else:
        print("{0} Year is not Leap Year".format(year))


    
