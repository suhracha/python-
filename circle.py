"""Example of Python program structure. 
Calculate Area and Circumference of circle using class."""
#Documentation section 
import math #import statement 
radius=5 #global declaration Section 
class Circle(): #class section 
    def getArea(self): 
        return math.pi*radius*radius 
    def getCircumference(self): 
        return radius*2*math.pi 
def showradius(): #sub Program section 
    print("Radius =",radius) 
showradius() #Playground Section 
c=Circle() 
print("Area =",c.getArea()) 
print("Circumference =",c.getCircumference())
