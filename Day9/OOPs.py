# OOP - Object oriented programming in python
# Some similar concept can be used in another languages too.
# Procedural programming language - all the work is done in serial form 
# But in oops 
# Due to fn the redundancy dec and reusability inc.
# A new level up is of oops.

# Class -> object 
# class - is a blueprint for creating the object
# eg. - student- name, age, etc  (class) 
#       s1 (object)

class Student:
    name = "karan"
    age = 20

s1 = Student()  # instance (object)
print(s1.name,s1.age,"\n",end = " ")
# print(s)

class Car:
    color = "blue"
    brand = "mercedes"

car1 = Car()
print(car1.brand)
print(car1.color)