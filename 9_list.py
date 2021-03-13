list1= ['가위','바위','보']
list2= [37, 23, 10, 33]

print(list1)
print(list2)

print(list1[1])
print(list2[3])


print(list1[-0])
print(list2[-0])

print(list1[-1])
print(list2[-1])

print(list1[-2])
print(list2[-2])

print(list1[-3])
print(list2[-3])

print( ' **************************************** ' )

list1 = [1,2,3,4,5]
print(list1)

list1.append(6)
print(list1)

list1+=[7]
print(list1)

list2=list1+[8,9,10,11,12]
print(list2)

n=13
ownership = n in list2
print(ownership)
print( 12 in list2)

del list2[11]
print(list2)
list2.remove(9)
print(list2)


