# function - is a block of statements that perform a specific task

# doing the same task multiple times 
# Function definition
def calculate_sum(a,b): # a,b are parameters
    sum = a+b
    print(sum)
    # return sum
calculate_sum(10,10) # function call; 10,10 are the arguments
calculate_sum(2,5)

calculate_sum(35,45)

# function printing the hello
def print_hello():
    print("Hello, Hacker is here")

print_hello()
print_hello()

# Average of 3 numbers
def average(a,b,c):
    avg = (a+b+c)/3
    print(avg)
# calling the average function
average(10,20,30) # it will print the value 20 
print(average(10,20,30)) # print the value None as it is 