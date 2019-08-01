'''
class object and method
'''

class TestClass:
    user_name=""
    user_email=""
    user_phone=""
    bonous=3090
    saalry=2000
    def __init__(self, name, email, phone):
        self.user_name= name
        self.user_email= email
        self.user_phone= phone

    def printInformation(self):
        print("Name is:", self.user_name)
        print("Email is:", self.user_email)
        print("Phone is:", self.user_phone)

    def calculateBonus(self):
        self.saalry= self.saalry*self.bonous
        print("Your salary total:", self.saalry)

    


obj2= TestClass("elias","abcd@gmail.com","+8801xxxx")
obj2.printInformation()
obj2.calculateBonus()




