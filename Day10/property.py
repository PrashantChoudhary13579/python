class student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math  
        self.percentage = str((self.chem  + self.math + self.phy) / 3) + "%"

    # def calculatePercentage(self):
    #     self.percentage = str((self.chem  + self.math + self.phy) / 3) + "%"

    @property
    def percentage(self):
        return str((self.chem  + self.math + self.phy) / 3) + "%"



stu1 = student(75,90,89)
print(stu1.percentage)

stu1.phy = 86
# stu1.calculatePercentage()
print(stu1.percentage)