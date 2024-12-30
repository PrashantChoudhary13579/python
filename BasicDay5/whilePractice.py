# practice using while loop 
"""
# 1. Print numbers from 1 to 100
i = 1
while i<= 100:
    print(i)
    i += 1

# 2. Print numbers from 100 to 1
i = 100
while i>= 1:
    print(i)
    i -= 1

# 3. Print the multiplication table of a number n

n = int(input("Enter the number"))
i = 1
while i <= 10:
    print(n,"*",i, "=",n*i)
    i += 1

# 4. Print the elements of the following list using a loop.
i = 1
nums = []
while i <= 10:
    nums += [i*i]
    i += 1
print(nums)
index = 0
while index < len(nums):
    print(nums[index])
    index += 1
"""
# 5. Searching for a number x in this tuple using loop

tup = ()
i = 1
while i<= 10:
    tup += (i,)
    i += 1
print(tup)
print(len(tup))
key = int(input("Enter the number you want to search"))
i = 0
while i < len(tup):
    if (tup[i] == key):
        print("Yes it is present at",i)
    i+=1   
   