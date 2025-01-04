

# Two mode for writing the file - write (w) and append (a)
# f = open("/workspaces/python/Day8/demo.txt","a")
#  we can open in "w" mode
# f.write("\nI am here to learn python and do something")

# f.close()

# f = open("Sample.txt","w")
# f.write ("Once you get everything cover then it will be easier for you to understand.")
# f.writelines("One day ")
# f.close()

f = open("/workspaces/python/Day8/Sample.txt","w+")  # it will overwrite in this mode
f.write ("Here") # w - only writing
# f.writelines("One day ")
# print(f.readline())
print(f.read())
# print(f.readable())
f.close()


