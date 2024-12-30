# Hello everyone, Here I, Prashant is here to make a new small project in Python using Dictionary data types, conditional statement and many more...

# Getting the name and phone number.


contacts ={
    "Prashant" : "7536004818",
    "Mummy" : "7536832182",
    "Papa" : "9756922181",
    "ChachuJi" : "9917633101"
}
index ={
    1 : "Add",
    2 : "Search",
    3 : "Delete",
    4 : "Display all",
    5 : "Exit"

}

print("What action do you want to perform ?")
print(" 1 : Add \n 2 : Search\n 3 : Delete\n 4 : Display all\n 5 : Exit")

action_1 = input("Enter the number ")

if action_1 in index:
    if action_1 == 1:
        name = str(input("Enter the name of the contact"))
        phoneNo  = int(input("Enter the phone number "))
        # new_Value = {"{name}": "{phoneNo}"}
        # contacts.update(new_Value)
        contacts.update({"name" : "phoneNo"})
    elif action_1 == 2:
        name = str(input("Enter the name of the contact"))
        phoneNo  = int(input("Enter the phone number "))
        new_Value = {"{name}": "{phoneNo}"}
        # for
    
else:
    print("Sorry, Please select the task among the following")