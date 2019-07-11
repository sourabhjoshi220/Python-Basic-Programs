def Remote_Control():
    yield "CNN"
    yield "ABC"
    yield 1
itr1=Remote_Control()
print(next(itr1))
print(next(itr1))
print(next(itr1))
#=============================

def nextSquare(i):

    i=0

    while True:
        yield i*i
        i+=1

for val in nextSquare(2):
    if val>100:
        break
    print("num is:",val)
        


#================

x='1:2:3'
print(x.split(':'))
#===================

x=[1,2,3,4]
print(x)
add=x.index(2)
print(add)

    


 
