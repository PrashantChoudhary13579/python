# string is  a data type.

str1 = "This is a string. "
str2 = 'Using single cot. '
str3 = """We can use triple too."""

# needs - when single cots and double cots are used inside the each other.
y = "lets's"
print(y)
# now you can getting some points why we are using this like this

# writing multiple lines in single string using escape sequence character.
str5 ="This is a string.\nWe are using the python to learn about string. "
print(str5)

# different operators for string
# concatenation
final_str = str1+str2+str3
print(final_str)

#length
print(len(final_str))
# here it is taking the values of length of the final_str in the form of integer which is good.
print(type(len(final_str)))
# or we have to taking these value in a variable and then find out all of it's thing.

#indexing is also available in python. Starting from 0 
str = "Prashant_Choudhary"
# str[4]= "A"
print(str[8])

#slicing - accessing a part of the string
print(str[5:8])
print(str[5:len(str)])
print(str[5:])
print(str[:9]) 

str = "white apple"
print(str[-len(str):-5])
print(str[-9:-5])
print(str[-5:])

# other functions in string.
str = "i am a hacker let's hack it."

print(str.endswith("it.")) #true.
print(str.endswith("er.")) #false.
print(str.capitalize())
str = str.capitalize()
print(str)
print(str.replace("hack","learn"))
print(str.find("hack"))
print(str.find("i"))
print(str.count("a"))
print(str.count("hack"))
