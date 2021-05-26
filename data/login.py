

from pyasn1.type.univ import Null
from pyrebase import pyrebase





Config = {
  "apiKey": "AIzaSyC1_YiXiG7iZEZDP3On60F9YpylViXChsQ",
  "authDomain": "vehicle-inventory-ae254.firebaseapp.com",
  "databaseURL": "https://manager-login-5b17a-default-rtdb.firebaseio.com/",
  "projectId": "vehicle-inventory-ae254",
  "storageBucket": "vehicle-inventory-ae254.appspot.com",
  "messagingSenderId": "388336737592",
  "appId": "1:388336737592:web:af0b61b4f1505c6940b5cd",
  "measurementId": "G-GQHKFQN7N6"
}

firebase=pyrebase.initialize_app(Config)
auth=firebase.auth()

class Login():
    def __init__(self):
        pass


    def login(self):
        while True:
            e=input("Email: ")
            p=input("Password: ")            
            if e and p !=Null:
                try:
                    auth.sign_in_with_email_and_password(e, p)
                    try:
                        print("You are sucessfull Login")
                        break
                    except:
                        print("Please Enter Correct Username and password")
                except:
                    print("Please Enter Correct Username and password")
            else:
                    print("Please Enter valid Email And password")

        
        


def main():
    s=Login()
    s.login()

main()