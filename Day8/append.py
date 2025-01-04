
# a - append mode

g = open("Day8/Sample.txt","a")
# print(g.read()) -- don't work in this 
g.write("In this world of hacker you are welcome !")
g.close()


# a+   - append plus mode

g = open("Day8/Sample.txt","a+")
print(g.read())  
g.write("In this world of hacker you are welcome !")
print(g.read())  
g.close()


# with syntax
with open("Day8/Sample.txt" ,"r") as f:
    data = f.read()
    print(data)

# deleting a file in python - it is done with the help of os module.
import os
os.remove("Sample.txt")