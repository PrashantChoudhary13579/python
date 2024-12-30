# We are haivng certain methods for dictionary

student ={
    "name": "Prashant",
    "score":{
        "Chemistry":95,
        "Physics":95,
        "Maths":99
        },
    "class" : 12,
    "school" : "Gita Niketan Awasiya Vidhyalay"
}

print(student.keys())
print(list(student.keys()))
print(len(student.keys()))

#values
print(student.values())

#items - we get the tuples
print(student.items())
print("\n")
pair = list(student.items())
print(pair[0])
print(pair[1])
print(pair[2])

#get - returns the key's value by sending the key
# print(student["name2"]) #print error
print(student.get("name2")) #print None

# we should always use the second one to avoid errors.

#update - pass the key value pair and add on to the dictionary
new_dict ={"city" : "kurukshetra"}
student.update(new_dict)
print(student)