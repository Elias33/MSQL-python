'''
inheritence
'''

class Test:
    exam_name=""
    exam_type=""

    def printInformation(self):
        print("This is print class of test")

class Test2(Test):
    def lastName(self):
        print("THis is last name")

    def printInformation(self):
        print("This is over riding.. modified")

obj2= Test2()
obj2.lastName()
obj2.printInformation()



