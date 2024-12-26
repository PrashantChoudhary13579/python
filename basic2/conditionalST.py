# if - elif - else (syntax)
age = 11
if(age>=18):
    print("You are enough mature.")
    print("You can vote and drive.")
else:
    print("Go home don't play outside.")

# Another example of if - elif - else (syntax)
light = "purple"
if(light == "red"):
    print("Stop. Don't go")
elif(light =="yellow"):
    print("Wait. It is about to Go")
elif(light =="green"):
    print("Ok. Go ahead")
else:
    print("Light is broken") # indentation  proper spacing is much more important.

print("End of the code.")

# if condition is always check while elif statment is checked only when if is failed.Else run when all the above conditions are failed.

# marks = float(input("Enter your marks - "))
# if (marks >= 90):
#     print("Scored - Grade : A")
# elif(90 > marks >= 80):
#     print("Scored - Grade : B")
# elif(80 > marks >= 70):
#     print("Scored - Grade : C")
# else :
#     print("Scored - Grade : D")

# Another way

# marks = float(input("Enter your marks - "))
# if (marks >= 90):
#     Grade = "A"
# elif(90 > marks >= 80):
#     Grade = "B"
# elif(80 > marks >= 70):
#     Grade = "C"
# else:
#     Grade = "D"
# print("Grade of the Student ->" ,Grade)

# talking about nesting - one statement containing the another statement.

age = 4
if(age>=18):
    if(age>=80):
        print("Can't Drive")
    else:
        print("Can Drive")
else:
    print("Can't Drive")