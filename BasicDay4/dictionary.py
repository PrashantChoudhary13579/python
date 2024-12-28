# data is stored in the form of dictionary

dict ={
    "name" : "Prashant",
    "cgpa" : 9.3,
    "marks": [93,95,91]
}
print(dict)
print(type(dict))
info = {
    "key" : "value",
    "name" : "Prashant",
    "learning" : "Python",
    "subjects": ["python","c++","java"],


}
dict["key"]= "Value"
print(dict)

# AS there is no indexing therefore it is unordered
# AS there we can make changes therefore it is mutable while tuples are not mutable
# As in this we are not having indexing or i can say they are unordered , therfore we don't allow duplicate keys
print(info["name"])
print(info["learning"])
print(info["subjects"])

# overwriting is possible 
# we can create a null dictionary 
# if we want to print the key that do not present then we will get error
