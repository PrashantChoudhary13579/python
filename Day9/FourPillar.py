# There are four pillars of oops - Abstraction, Encapsulation, Inheritance, Polymorphism
class car:
    def __init__(self):
        self.acc = False
        self.brake = False
        self.clutch = False

    def start (self):
        self.clutch = True  # Unnecessary things got hidden
        self.acc = True
        print("car started") # Things i want to see 

car1 = car()
car1.start()

