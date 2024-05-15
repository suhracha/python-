class Grandfather: 
    def __init__(self): 
        print("Grand Father") 
#The child class Father inherits the base class Grandfather 
class Father(Grandfather): 
    def __init__(self): 
        Grandfather.__init__(self)
        print("Father") 
#The child class Son inherits another child class Father 
class Son(Father): 
    def __init__(self): 
        Father.__init__(self)
        print("Son") 
s1=Son() 