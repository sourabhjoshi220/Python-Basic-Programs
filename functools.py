import functools
list=[1,2,3,4,5,6,2]

print("the sum of the list is: ", end=" ")
print(functools.reduce(lambda x, y: x+y, list))

print("the maximum element inside the list is: ", end=" ")
print(functools.reduce(lambda x,y : x if x > y else y,list))

