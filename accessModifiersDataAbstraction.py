class student: 
    __a=10 #private variable 
    b=20 #public variable 
    def __private_method(self): #private method 
        print("private method is called") 
    def public_method(self): #public method 
        print("public method is called") 
        print("a=",self.__a) #can be accessible in same class 
s1=student() 
# print("a=",s1._ _a) #generate error 
print("b=",s1.b) 
# s1._ _private_method() #generate error 
s1.public_method() 