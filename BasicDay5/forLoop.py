# for loop - is used when we have to traverse sequentially 
nums = [1,2,3,4,5]
for i in nums:
    print(i)

veg = ["potato", "brinjal","ladyfinder","gobhi","kadu"]
for v in veg:
    print(v)
# it is printing the list 

values = (2,4,6,8,6,4,3,1)
for va in values:
    print (va)
# it is printing the tuples too.

str = "Prashant"
for char in str:
    print (char)

# finding where should else be used ? - when using break/continue..
for char in str:
    if(char == 'n'):
        print("n found")
        break
    print(char)
else:
    print("End")


# range() function
