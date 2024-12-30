# Hello Everyone, This is a mini project made by Prashant which is showing the menu status and the order you want in a Restaurant

# Defining the menu of restaurant
menu ={
    "Chhole Bhature" : 60,
    "Samosa" : 10,
    "Tea" : 20,
    "Coffee" : 50,
    "Rice Plate" : 45,
    "Dosa" : 110
}

#Greeting
print("Welcome to CHOUDHARY'S Restaurant \n")

# Showing the Menu bar
print("Chhote Bhature : Rs60  \nSamosa : 10  \nTea  : 20 \nCoffee : 50 \nRice Plate : 45 \nDosa : 110")

# Defining the Total order variable
totalOrder = 0

#Getting the first item
item_1 = input("Enter the name of item you want to order = ")
# Checking the item present in the menu
if item_1 in menu:
    totalOrder += menu[item_1]  # 0 + 60
    print(f"Your item {item_1} has been added to your order\n")

else:
    print(f"Order item {item_1} is not available yet!\n")

# Asking for another order.
another_Order = input("Do you want to add another item ? (Yes/No) \n")

#IF yes then getting the another order and also addiing the cost of it.
if another_Order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        totalOrder += menu[item_2]  # 60 + 20
        print(f"Your item {item_2} has been added to your order\n")

    else:
        print(f"Order item {item_2} is not available yet!\n")

# Printing the total amount 
print(f"Total amount you have to pay : {totalOrder:.2f}")
