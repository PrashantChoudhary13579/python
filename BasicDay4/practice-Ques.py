# 1. Storing the word meanings in a python dictionary
dictionary = {
    "table" : ("a piece of furniture","list of facts and figure"),
    "cat " : "a small animal",
}
# we can store the meaning of table in two ways -  list or tuple.
print(dictionary)

# 2. You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.

subject = {"python","java","c++","python","javascript","java","python","java","c++","C"}
# we will use the set as we want the unique values
classroom = len(subject)
print("No. of classrooms - ", classroom)

# 3. WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
# start with an empty dictionary and add one by one . use subject name as key and marks as value.

