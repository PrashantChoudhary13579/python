# Create student class that takes name and marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class student:
    # constructor
    def __init__(self,fullname,marks):
        self.name= fullname
        self.marks = marks
    
    # Method
    def get_average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi,",self.name,"Your avg score is",sum/3)
    
s1 = student("Prashant",[99,98,97])
# print()
s1.get_average()

# We have to create account class with 2 attributes - balance and account no.
# Create methods for debit, credit and printing the balance

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit (self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("Total balance =",self.get_balance())

    # credited method
    def credit (self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("Total balance =",self.get_balance())
    
    def get_balance(self):
        return self.balance

acc1 = Account(10000,12345)
print(acc1.balance)
# print(acc1.account_no)

acc1.debit(1000)
acc1.credit(500)

acc1.credit(400000)
acc1.debit(45000)