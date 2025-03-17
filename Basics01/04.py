#List --> lists act as dynamic array, where you can add more items on the fly.
# list is hetergeneous . Can store different data type in a same list.

# Memory requiirement is more in lists than array.
# Accesing elements in array is faster, while lists are slower.

# lIsts are referential array. You are not directly storing the values, but storing the 
# addresses of the objects stored in the list

# Lists are ordered. Lists are mutable. can have duplicates. heterogeneous .items can be 
# accessed. Can be nested.

# Adding elemets to the liost
# 1. append()--> Adds a single element to the end of the list.

# l1 = [1,2,'bucket',[3,4]]
# print(l1)
# print(l1[3][1])

# l2 = [True,0,1.2,5+5j,'Kolkata']
# print(id(l2),type(l2))

# l1 = [1,2,3]
# print(id(l1))
# print(id(l1[0]))
# print(id(1))

# print(list("Hello"))

# l1 = [1,3,5,7]
# # print(l1[0:3])
# # print(len(l1))

# l1.append(True)
# print(id(l1))
# l1.append([4,[5,6,[7,8,9,[10,11]]]])
# print(id(l1))
# l1.extend(list("Hello"))
# print(id(l1))

# l2 = [3,4,6,8,True,False]
# l2[4] = 0
# print(l2)

# l3 =[1,2,3,4,5,6]
# print(id(l3))
# l3[1:4]= [100,200,300]
# print(l3)
# print(id(l3))

l = [2,5,7,9,10]
print(l,id(l))
del(l[3])
print(l,id(l))

# print(l.remove(5))
print(l)

list1 = [1,2,3.7,True,'Sayan',[5,6],7+9j]
for i in list1:
    if i == [5,6]:
        continue
    print(i,end =" ")
print()

print(len(list1))
list2 = [2,4,1,2,89,76]
print(list2,id(list2))
print(sorted(list2),id(sorted(list2)))


