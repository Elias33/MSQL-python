'''
Python object oriented
'''

class User:
    name="";
    email="";
    password="";
    login= False

    def login(self):
        email= input("Enter email:\n")
        password= input("Enter the password:\n")
        if email== self.email and password== self.password:
            login= True
            print("Login successfully")
        else:
            print("login failed")


    def logout(self):
        login= False
        print("Logged out")


    def isloggedin(self):
        if self.login:
            return True
        else:
            return False

    def profile(self):
        if isloggedin():
            print(self.email, "\n", self.password)
        else:
            print("User not loggin")


user1= User()
user1.email="umme"
user1.password="umme1234"
user1.login()


