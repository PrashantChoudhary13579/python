# Constructor - invoke when a new object is formed 
# It is init function
class student:

    college_name = "UIET"
    # Default constructors
    def __init__(self):
        pass

    # Parameterized constructors
    def __init__(self, fullname,marks):
        # print(self) 
        self.name = fullname
        self.marks = marks
        print("Adding new student in the Database")
    
s1 = student("Karan",99)
print(s1.name,s1.marks,s1.college_name)

# Self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

s2 = student("Prashant",95)
print(s2.name,s2.marks)

# The data , variables which we stored/ send is known as attributes.

# We uses self for each different values 
# name and age will be used as self.____. Therefore it is instance