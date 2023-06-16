#positional arguements
#Ex1:
# def fun(i,j):
#     print(i,j)
# fun(10,20)

#Ex:2
# def fun(i,j=10):
#     print(i,j)
# fun(100,200)
# fun(100)

#Keyword arguements
#Ex1
# def fun(i,j):
#   print(i,j)
# fun(j=20,i=10)

#Ex2
# def greeting(name,greetmsg):
#     print(greetmsg+"   "+name)
# # greeting(name='John',greetmsg='Hello')
# greeting(greetmsg='Hello',name='John')

# Ex4: combintion of positinal  and keyword parameter

# def my_fun(a,b,c):
#     print(a,b,c)
# my_fun(10,20,30)
# my_fun(10,b=20,c=30)
# my_fun(b=20,a=10,c=30)
# my_fun(10,20,c=30)
# my_fun(10,b=20,30) #syntax error

#Ex:5  function can return multiple values.
# def largest(a,b):
#      if a>b:
#       return a,b
#      else:
#       return b,a
# print(largest(100,200))
# print(largest(20,10))   

# res=largest(10,20)
# print(res)
# print(type(res))





