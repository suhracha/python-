class Counter: 
    __secretCount = 0 #private variable 
    def count(self): #public method 
        self.__secretCount += 1 
        print('count= ', self.__secretCount) #can be accessible in the same class 
c1= Counter() 
c1.count() #invoke method 
c1.count() 
print("Total count=" , c1.__secretCount) #cannot access private variable directly 