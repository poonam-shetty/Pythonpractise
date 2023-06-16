#creating dictionary

# mydic={101:"x",102:"y",103:"z"}
# print(mydic)

# To access the items from the dictionary
# mydic={"brand":"hyundai","model":"i10","year":2020}
# #way1
# print(mydic["brand"])
# print(mydic["model"])
# print(mydic["year"])

#using get()
# mydic={"brand":"hyundai","model":"i10","year":2020}
# #x=mydic.get("brand")
# print(mydic.get("brand"))

#Change values in the dictionary
mydic={"brand":"hyundai","model":"i10","year":2020}
print(mydic)
mydic["year"]=2021
print(mydic)

#Reading item from dictionary using loop
# mydic={"brand":"hyundai","model":"i10","year":2020}
# for i in mydic:
#     print(i)

# mydic={"brand":"hyundai","model":"i10","year":2020}
# for i in mydic:
#     print(mydic[i])

# mydic={"brand":"hyundai","model":"i10","year":2020}
# for i in mydic.values():
#    print(i)

# mydic={"brand":"hyundai","model":"i10","year":2020}
# for x,y in mydic.items():
#     print(x,y)


#Want to check key is exist in dictionary or not?
# mydic={"brand":"hyundai","model":"i10","year":2020}
# if "mode" in mydic:
#     print("exist")
# else:
#     print("not exists")

# Find number of items in dictionary
# mydic={"brand":"hyundai","model":"i10","year":2020}
# print(len(mydic))

# Adding items to dictionary
# mydic={"brand":"hyundai","model":"i10","year":2020}
# mydic["color"]="red"
# print(mydic)

#remove item from dictionary
#using pop()
# mydic={"brand":"hyundai","model":"i10","year":2020}
# mydic.pop("year")
# print(mydic)

#using del keyword
# mydic={"brand":"hyundai","model":"i10","year":2020}
# del mydic["year"]
# print(mydic)

#To delete entire dictionary
# mydic={"brand":"hyundai","model":"i10","year":2020}
# del mydic
# print(mydic)


# #using clear()
# mydic={"brand":"hyundai","model":"i10","year":2020}
# mydic.clear()
# print(mydic)

#Coping dictionary
mydic1={"brand":"hyundai","model":"i10","year":2020}
print(mydic1)
mydic2=mydic1
print(mydic2)


#Using copy()
mydic1={"brand":"hyundai","model":"i10","year":2020}
print(mydic1)
mydic2=mydic1.copy()
print(mydic2)
