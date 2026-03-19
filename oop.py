#what is a oop?
#oop is way of writing code using objects and classes.

#key concepts of oops
#blueprint(design)

#ex:
#class student:
#pass

#2.object:
#"class = design,object =real thing"

#3. constrctor:(__init__)
#automatically runs when object is created

class student:
    def __init__(self, name):
        self.name = name
s1 = student("preksha")
print(s1.name)


#TASKS:
#1. # Task:
# create  a Class "Car" with constructor to initialize "brand"
# and a method "drive" that prints "Driving" {brand}.
class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"Driving {self.brand}")

car1 = Car("Toyota")
car1.drive()

#2. create a class "employes"with constructor to intialzation "first name","last name","age",and "role" and "salary" and a method "work"that prints "{first name}"{last name}is working  as {role} with salary {salary}"

class Employees:
    def __init__(self, first_name, last_name, age, role, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.role = role
        self.salary = salary

    def work(self):
        print(f"{self.first_name} {self.last_name} is working as {self.role} with salary {self.salary}")
emp1 = Employees("John", "Doe", 30, "Software Engineer", 50000)
emp1.work()

#3. 

