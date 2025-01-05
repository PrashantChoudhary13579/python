class student:
    def __init__(self,name):
        self.name = name

s1 = student("Prashant")
print(s1.name)
del s1.name # we can use the del keyword to delete any attribute or any object.
print(s1)

# Public - accessing the attribute / method outside the class
# and private - accessing the attributes/ method only inside the class
class Account:
    __name = "anonymous"

    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # it become private

    def reset_pass(self):
        print(self.__acc_pass)

    def __hello(self):
        print("Hello, person!")

    def welcome(self):
        self.__hello()

acc1 = Account("12345","abcde")
print(acc1.acc_no)
print(acc1.reset_pass())
# Things which are declared as public have higher chance of error or mistake 
# Therefore we should make  the acc_pass as private not public

# p1 = Account()
print(acc1.welcome())
