pytuple1=(1,2,3,4,6)
pytuple2=(10,20,30,40,50)

for x,y in zip(pytuple1, pytuple2):
    print("{}+{}={} is the addition".format(x,y,x+y))

#======================================================

pytuple=[1,2,3,4]
pytuple2=[2,5,6,9]

pyzip=zip(pytuple, pytuple2)
print(tuple(pyzip))

pyunzip= zip(*pyzip)
print(tuple(pyunzip))


#==================
from random import shuffle
a=["A","B","C","D","E"]
shuffle(a)
print(a)
