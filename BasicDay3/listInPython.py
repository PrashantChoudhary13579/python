# In this we will cover the list and tuples.
# List is similar to the array in other language.
marks = [94.5,87.5,95.2,66.4,85.7]
print(marks)
print(type(marks))

# properties are similar to string
print(marks[0])
print(marks[1])

student = ["karan Aujla",32,"Punjab"]
print(student)
print(student[0])
print(student[1])
print(student[2])
print(len(student[2]))

print(type(student[0]))
print(type(student[1]))
print(type(student))

# strings are immuable and there values can't be change
# while the list are mutable and we can change the values in it.

student[0]= "Gur Sidhu "
print(student)

# As the string has slicing in the same way list also has slicing in python
#  
print(marks [2:4])
print(marks[:5])
print(marks[1:])
print(marks[-3:-1])