# 1. Creating a new file "practice.txt" using python. And adding the following data in it.

# file = open("/workspaces/python/Day8/practice.txt","r+")
# file.write ("Hi everyone\n")
# file.write ("we are learning File I/O\n")
# file.write ("using Java\n")
# file.write ("I like programming in Java\n")

# file.seek(0)

# data = file.read()
# print(data)
# # print(file.read())
# file.close()

#2. WAF that replace all occurrences of "Java" with "Python" in above file
file_path = "Day8/practice.txt"

def changing(file_path,old_str,new_str):
    # reading the file
    with open("Day8/practice.txt","r") as f:
       data = f.read()
    
    # changing the data
    new_Data = data.replace(old_str,new_str)

    # writing in the file
    with open("Day8/practice.txt","w") as g:
        g.write(new_Data)

# changing(file_path,"Java","Python")

# 3. Search if the word "learning" exists in the file or not.

# with open( "Day8/practice.txt","r") as f:
#     data = f.read()
#     word = "learning"
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not found")

# 4. WAF to find in which line of the file does the word "learning" occur first. Print -1 if word not found.

def check_for_line (word):
    data = True
    line_no = 1
    with open("Day8/practice.txt") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
            line_no += 1
    return -1

# print(check_for_line("pythl"))

with open("Day8/practice.txt","r") as f:
    data = f.read()
    print(data)
    print(type(data))
    
    # num = ""
    # for i in range(len(data)):
    #     if (data [i] ==","):
    #         print(int(num))
    #         print(type(num))
    #         num =""
    #     else:
    #         num +=  data[i]

    nums = data.split(",")
    count = 0
    for val in nums:
        if(int(val)%2 == 0):
            print(val)
            count += 1

    print("Total no. of even number are",count)