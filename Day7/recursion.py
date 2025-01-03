# recursion - a function calling itself again and again

# all the work which we do through loops can be done with the help of recursion

# def show (n):
#     if(n == 0 ):
#         return
#     print(n)
#     show(n-1)
# show(5)

# factorial in recursion
# def fact (n):
#     if(n==1 or n==0):
#         return 1 
#     else:
#         return n * fact (n-1)

n = int(input("Enter the number"))
# value = fact (n)
# print(value)

# 1. WARF to calculate the sum of first n natural number
def sum (n):
    if(n == 1 ):
        return 1 
    else:
        return n + sum (n-1)

print(sum(n))

# 2. WARF to print all the element in a list 
animal = ["buffalo","cow","horse","zebra","pig","tiger","Elephant"]
index = 0
# data = len(animal,index)
def listing(animal,index):
    if(index == len(animal)):
        return
    print( animal[index] )
    listing(animal,index + 1)

listing(animal,index)