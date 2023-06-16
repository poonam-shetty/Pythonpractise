#how to create tuple
# mytuple=("apple","banana","cherry")
# print(mytuple)

#Access indivitual item from the tuple

# mytuple=("apple","banann","cherry")
# print(mytuple[1])
# print(mytuple[-1])

#specify the range of indexes.
# mytuple=("apple","banana","orange","kiwi","melon","mango")
# print(mytuple[2:5])
# print(mytuple[-4:-1])

#changing the tuple items

# mytuple=("apple","banana","cherry")
# mylist=list(mytuple)
# mylist[0]="orange"
# mytuple=tuple(mylist)
# print(mytuple)

#Reading tuple items using loop
# mytuple=("apple","banana","cherry")
# for i in mytuple:
#     print(i)

#To check item is present in tuple or not
# mytuple=("apple","kiwi","cherry")
# if "banana" in mytuple:
#     print("yes","banana is present")
# else:
#     print("no","banana is not present")


#tuple length counting items in a tuple

# mytuple=("apple","banana","cherry")
# print(len(mytuple))

#add item to the tuple
# mytuple=("apple","banana","cherry")
# mytuple[0]="orange"
# print(mytuple) # type object doesnt support item assignment#


#copy tuple
# mytuple1=("apple","banana","cherry")
# mytuple2=mytuple1
# print(mytuple2)
# print(mytuple1)

#removing item from tuple
# mytuple=("apple","banana","cherry")
# mytuple.remove("apple")

#deleting tuple
# mytuple=("apple","banana","cherry")
# del mytuple
# print(mytuple)

#joining or combine tuples
# tuple1=(10,20,30)
# tuple2=('a','b','c')
# tuple3=tuple1+tuple2
# print(tuple3)

#compare 2 tuples equal or not

# tuple1=(10,20,30)
# tuple2=('a','b','c')
# if tuple1==tuple2:
#   print("tuples are equal")
# else:
#   print("tuples are not equal")   