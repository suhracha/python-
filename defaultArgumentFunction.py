class Demo: 
    def arguments(self, a = None, b = None, c = None): 
        if(a != None and b != None and c != None): 
            print("3 arguments") 
        elif (a != None and b != None): 
            print("2 arguments") 
        elif a != None: 
            print("1 argument") 
        else: 
            print("0 arguments") 
obj = Demo() 
obj.arguments("Meenakshi","Anurag","Thalor") 
obj.arguments("Anurag","Thalor") 
obj.arguments("Thalor") 
obj.arguments()