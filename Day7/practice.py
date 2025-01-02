
# 1. WAF to print the length of a list.
listing = [3,5,6,7,8,5,0,7]
# making the function of name list_len 
def list_len(list): # list as parameter
    return (len(list)) # returning the length

leng = list_len(listing) # saving the return value in leng variable
print(leng) # printing the leng 

# 2. WAF to print the elements of a list in a single line. (list is the parameter)
def list_ele(list):
    for i in list:
        print(i,end=" ")
        i += 1
    
list_ele(listing)

# 3. WAF to find the factorial of n (n is the parameter)

# using iteration
# def factorial (n):
#     fact = 1
#     while n >= 1:
#         fact *= n
#         n -= 1
#     return fact
    
# # Taking input
# n = int (input("Enter the number"))
# # putting in a variable
# value = factorial(n)

# # print(value)
# print(f"Factorial of ",n,"is",value)

# using recursion
# print("Using recursion")
# def fact (n):
#     if (n <=1):
#         return 1
#     else:
#         return n * fact(n-1)
    
# # for input
# n = int(input("Enter the input values"))
# # for printing
# print(fact(n))

# 4. WAF to convert the USD to INR

def convertor( usd ):
    inr = 85.5 * usd
    print("USD =", usd)
    print("INR =", inr)

convertor(1500)

# 5. Checking whether a number is odd or even
num = int(input("Enter the number"))
def EvenOdd(num):
    if (num % 2 == 0):
        print("Number is even")
    else:
        print("Number is odd")

EvenOdd(num)