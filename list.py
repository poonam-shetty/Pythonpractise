#List 
#Ex1:How to create List

# mylist1=[10,20,30,40,50]
# mylist2=["apple","Banana","cherry"]
# mylist3=["apple",10,"banana",20]
# mylist=list()

# #to print value from the list
# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist2)


#How to accessing items from the list
# mylist=["apple","banana","cherry"]
# print(mylist[0])
# print(mylist[2])
# print(mylist[-3])


#Range of indexes
mylist=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(mylist[2:5])
print(mylist[-4:-1])
print(mylist[-4:-2])

#How to change item value
# mylist=["apple","banana","cherry"]
# print(mylist)
# mylist[0]="orange"
# print(mylist)

#read the list items using loop
# mylist=["apple","banana","cherry"]
# for i in mylist:
#  print(i)

#Check if the item is exists in the list or not
# mylist=["apple","banana","cherry"]
# if "apple" in mylist:
#     print("yes.apple is present")
# else:
#         print("no,apple is not present")

#list length
# mylist=["apple","banana","cherry"]
# print(len(mylist))

#add items appen() insert()
# mylist=["apple","banana","cherry"]
# mylist.append("orange")
# print(mylist)

# mylist=["apple","banana","cherry"]
# mylist.insert(0,"orang")
# print(mylist)

#remove item from the list
# pop()
# mylist=["apple","banana","cherry"]
# mylist.pop(2)
# print(mylist)

#del()
# mylist=["apple","banana","cherry"]
# del mylist[2]
# print(mylist)

#clear()
# mylist=["apple","banana","cherry"]
# mylist.clear()
# print(mylist)

#copy list 
#1.By using list functions

# mylist1=["apple","banana","cherry"]
# mylist2=list(mylist1)
# print(mylist1)
# print(mylist2)

#copy()
# mylist1=["apple","banana","cherry"]
# mylist2=mylist1.copy()
# print(mylist1)
# print(mylist2)

#combine/join the lists
#using + operator
# list1=["a","b","c"]
# list2=[1,2.3]
# list3=[list1+list2]
# print(list3)

# #using loop statement
# list1=["a","b","c"]
# list2=[1,2,3]
# for i in list2:
#     list1.append(i)
#     print(list1)

#using extend()
list1=['a','b','c']
list2=[1,2,3]
list1.extend(list2)
print(list1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             