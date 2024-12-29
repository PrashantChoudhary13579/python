# Here we will discuss the set method 
# set are mutables but the element in the set are immutable (we can't change them)
set = {1,2,3,4,5}

# add the element
set.add(6)
set.add(7)
set.add("Engineering Student")
# set.add([1,2,3])
# We can't add the list as it is mutable but we can add the list
set.add((1,2,3))
print(set)

# remove the element
set.remove(1)
# set.remove(10)
print(set)

# removing a random value
# print(set.pop())
print(set.pop())
print(set.pop())
print(set.pop())
print(set)

set2 = {"hello", "giyan","ramprasad",2,5,7}
# printing the union - same as maths 
print(set.union(set2))
#printing the intersection - same as maths
print(set.intersection(set2))
