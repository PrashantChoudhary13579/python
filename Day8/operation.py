#  The basic operation to do on a file are 
#  1. Opening the file
#  2. Reading the file
#  3. Closing the file

# f = open("file_name","mode")

#  file_name = will be replaced by the name of the actual file 
# mode will be replaced by the name of the mode in which u want to open the file.

f = open("/workspaces/python/Day8/demo.txt","r")

#  read() - read the full file 
#  readline() - read the single line

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

print(type(line1))

f.close() 

"""
r - open for reading
w - open for writing, first truncating the file
x - create a new file and open in writing
a - open for writing, appending to the end
b - binary mode
t - text mode
+ - open a disk file for updating (r/w)

"""
