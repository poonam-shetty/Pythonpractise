#creating class

# class MyClass:
#    def myfun(self):
#       pass
#    def display(self):
#       print("john")
# mc1=MyClass()
# mc1.myfun()
# mc1.display()

#Ex2:Instance and static method
# class MyClass:
#      def m1(self):
#         print("This is instance method..")
#      @staticmethod
#      def m2(self,num):
#         print(self,num)
# mc=MyClass()
# mc.m1()
# mc.m2(10,20)
# MyClass.m2(100,200)

# Ex3:Global,class,local variable

# class myclass:
#    a,b=10,20
#    def add(self):
#      # print(a,b) #gives error,we cannot access class variable inside method
#       print(self.a+self.b)
#    def mul(self):
#       print(self.a*self.b)   
# mc=myclass()
# mc.add()    
# mc.mul()
