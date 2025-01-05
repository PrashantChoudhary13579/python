# Inheritance - when one class (child) derives the properties and methods of another class(parent/base)
# child class - which takes the properties
# parent class - which gives the properties
# Inheritance - 1. Single 
#               2. Multi-level 
#               3. Multiple

class Car:
    
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("Car stopped...")
    
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    color = "black"
    def __init__(self, type):
        self.type = type



car1 = Fortuner("Diesel")
car2 = ToyotaCar("Prius")

# print(car1.brand)
print(car1.start())
print(car1.color)


class A:
    var1 = "Welcome to class A"
class B:
    var2 = "Welcome to class B"

class C(A,B):
    var3 = "Welcome to class C"

c1 = C()

print(c1.var1)
print(c1.var2)
print(c1.var3)