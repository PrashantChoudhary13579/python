# 1. WAP to ask the user to enter names of their 3 favorite movies and store them in a list.
# list = []
# print("Enter the name of 3 favorite movies ")

# a = input("first - ")
# b = input("Second - ")
# c = input("Third - ")

# list.append(a)
# list.append(b)
# list.append(c)
# print(list)

#2. WAP to check if a list contains a palindrome of elements . 
# list = [1,"abc","cba",1]
# print(list)
# # list.reverse()
# list2 = list.copy()
# list2.reverse()
# print(list2)

# if(list == list2):
#     print("Pallindrome")
# else:
#     print("Not Pallindrome")

#3. WAP to count the number of students with the "A" grade in the following tuple.
tuple =("C","D","A","A","B","B","A")

print("No of students with A grade =",tuple.count("A"))

#4. Store the tuple into list and sort them form "A" to "D"
firstList = list(tuple)
# firstList = [x for x in tuple]
print (firstList)
firstList.sort()
print(firstList)
