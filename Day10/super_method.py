class Car:
    def __init__(self,type):
        self.type = type
    
    @ staticmethod
    def start():
        print("Car started")
    
    @ staticmethod
    def stop():
        print("Car Stopped ")
    
class ToyotaCar(Car):
    def __init__(self, name,type):
        self.name = name
        super().__init__(type)
        # By using the super we can call the methods from the parent class

car1 = ToyotaCar("Prius","electric")
print(car1.type)

# class method - 

class Person:
    name = "anonymous"

    # def changeName(self,name):
        # Person.name = name
        # self.__class__.name = name
        # This is creating the new name/instance.
    
    @classmethod
    def changeName(cls, name):
        cls.name = name
    
p1 = Person()
p1.changeName("Rahul Choudhary")
print(p1.name)
print(Person.name)

# 1. static method (only printing not argument)
# 2. class method (cls as an argument)
# 3. Instance method(self as an argument)