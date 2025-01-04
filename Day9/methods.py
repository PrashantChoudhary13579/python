# class - 1. Data - (attributes)
#       - 2. Methods - are the functions that belong to objects.

class student:
    college = "UIET"
    Batch = "2023-27"
    Class = "CSE"
    # constructor
    def __init__(self,fullname,age,marks):
        self.name = fullname
        self.age = age
        self.marks = marks
    
    # Methods

    def hello (self):
        print("Hello ,",self.name)
    def marking(self):
        print("Your marks are",self.marks)

    # static  methods - do not contain self parameter
    # - works at class level
    @staticmethod
    def college():
        print("Our college is UIET")

# Creating an object 
s1 = student("Prashant",20,95)
s1.hello()
s1.marking()
s1.college()
# print(s1.marks())