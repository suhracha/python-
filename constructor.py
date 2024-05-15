class Person: 
    def __init__(self, rollno, name, age): 
        self.rollno=rollno 
        self.name = name 
        self.age = age 
        print("Student object is created") 
p1 = Person(11,"Vijay", 40) 
print("Rollno of student= ", p1.rollno) 
print("Name of student= ",p1.name) 
print("Age of student= ",p1.age)