# loops - repeating the things

# while (reserved keyword) loops 
# i = 1
# while i<=100:
#     print(i, "Hello")
#     i += 1
# # print(i)

# # flow - while - condition - work and loop go on by inc./dec. until condition is false

# # In reverse
# j = 10
# while j>=1:
#     if(j == 8):
#         j-=1
#         continue
#     # if(j==5):
#     #     break
#     print (j)

#     j -= 1
# print("End of the loop")

# printing the odd number by applying the continue
print("Printing the odd numbers")
i = 1
while(i <= 10 ):
    if(i %2 == 0):
        i += 1
        continue
    else:
        print(i)
    i += 1

# if we wish to print the even numbers 
print("Printing the even numbers")
i = 1
while(i <= 10):
    if(i %2 != 0):
        i+= 1
        continue
    else:
        print(i)
    i += 1
