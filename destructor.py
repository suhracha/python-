class Student: 
    def __init__(self): 
        print('non parameterized constructor-student created ') 
    def __del__(self): 
        print('Destructor called, student deleted.') 
s1=Student() 
s2=Student() 
del s1 
s2.__del__