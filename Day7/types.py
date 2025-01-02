# functions are basically of two types - 
# 1. build-in function - build(), len(), type(), range()
# 2. user define function 

print("prashant","choudhary") # sep = " "
print("Gujjar","prashant", sep= "",end = " ")
print("choudhary") # end = "\n"

# Default parameters
def cal_prod(a= 6,b=5):
    print(a * b)
    return a * b
# hum ek ko bhi default bana sakte 
cal_prod()