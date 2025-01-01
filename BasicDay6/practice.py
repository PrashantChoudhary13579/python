# 1 . printing numbers from 1 to 100

# for val in range(1,101):
#     print(val)

# 2. Printing numbers from 100 to 1.

# for val in range(100,0,-1):
#     print(val)

# 3. Printing the multiplication table 
# num = int (input("Enter the number"))
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)

# 4. Write a program to find the sum of first n numbers (using while)

val = 1
sum = 0
n = int (input("Enter the value "))
while val <= n:
    sum += val
    val += 1
print(sum)

# 5. WAP to find the factorial of first n numbers.(using for)
i = 1
n = int (input("Enter the value"))
fact = 1
for i in range(1,n+1):
    fact = fact * i 
print("Factorial of i =",fact)