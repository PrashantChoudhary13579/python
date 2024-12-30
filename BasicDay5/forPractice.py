# 1. Print the element of the following list using a loop

number = [1,4,9,16,25,36,49,64,81,100]
for n in number:
    print(n)

# 3. Search for a number x in this tuple using loop
x = int (input("Enter the number "))
for n in number:
    if (x == n ):
        print("Number is present")
if( x != n):
    print("Number is not present")
