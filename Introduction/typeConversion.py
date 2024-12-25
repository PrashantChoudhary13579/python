# Here we are going to learn about the type conversion - Converting one data type into another data type (automatically)
# type casting - (if done manually)

a = 2
b = 4.56
sum = a + b
print(sum)
# float > int (float is superior than int)

# if we take a string then 
a = "2"
b = 45
# sum = a+b
# print(sum) - Error : Because a string can't be converted into a number automatically 
# Solution - apply type casting

a = float("2") # character can'' be converted. Only values will be converted.
b = 15.234
add = a +b
string = str(add)
print(add)
print(type(add))
print(string)
print(type(string))

