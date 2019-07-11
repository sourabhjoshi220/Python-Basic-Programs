def extendList(val, list=[2]):
    list.append(val)
    return list
list1=extendList(10)
print(list1)
list2=extendList(103.00,[])
print(list2)
list3=extendList('a')
print(list3)
list4=extendList('sourabh')
print(list4)
list5=extendList(0)
print(list5)

