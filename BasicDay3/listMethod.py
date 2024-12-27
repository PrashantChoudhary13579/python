# In this we are learning about the methods which we are using in the list
list = ["anshika","deepak","adhyay"]
# we can use anything - number, string, character, etc
print(list)
print(type(list))

# Here we are appending - which means we are adding something to it.
list.append("anurag")
print(list)

# Here we are sorting the list using the sort function
list.sort()
print(list)

# In this sorting is done in the decreasing order
list.sort(reverse = True)
print(list)

# In this we will reverse the given list
list.reverse()
print(list)

# If we have to insert the element at a particular index
list.insert(2,'prashant')
print(list)