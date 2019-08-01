'''
user test data
'''

class User:
    name=""
    email=""
    password=""
    login= False
    def checkLogin(self):
        email= input("Enter user name")
        password= input("Enter password")
        if email== self.name and password== self.password:
            login= True
            print("Login successfully")
        else:
            print("Login is not correct")

    def isLoggedIn(self):
        if self.login:
            print("Loggin")
        else:
            print("Is not loggin")
    def profile(self):
        if isLoggedIn():
            print(self.name,"\n", self.password)
        else:
            print("user is not loggin")

user1= User()
user1.name="elias"
user1.password="umme"
user1.checkLogin()
