import re, random
from uuid import uuid4
from pyasn1.type.univ import Null
from pyrebase import pyrebase
import mysql.connector
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='vehicle'

)

mycursor=mydb.cursor()

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

Config = {
  "apiKey": "AIzaSyDKRuAbcMNphIOq594lsGjE5yYi3l84G4U",
  "authDomain": "manager-login-5b17a.firebaseapp.com",
  "databaseURL" : "https://manager-login-5b17a-default-rtdb.firebaseio.com/",
  "projectId": "manager-login-5b17a",
  "storageBucket": "manager-login-5b17a.appspot.com",
  "messagingSenderId": "922034688200",
  "appId": "1:922034688200:web:6c3ca75b84e1a06c0fd5fd",
  "measurementId": "G-75L9V8RDRR"
}

firebase=pyrebase.initialize_app(Config)
auth=firebase.auth()
db=firebase.database()
class signup():
    def __init__(self):
        signup.email=()
        signup.password=()
        signup.employee_id=()
        signup.first_name=()
        signup.last_name=()
        signup.phone=()



    def signup(self):
        fname=input("Please Enter Your First Name Here: ")
        if type(fname)==str:
            try:
                signup.first_name=fname
            except:
                print("Please Enter Your name only")
        lname=input("Please Enter Your Last name Here: ")
        if type(lname)==str and lname!=fname:
            try:
                signup.last_name=lname
            except :
                print("Please Enter Your Last name only")
        phone = (input("Please Enter a Phone Number along Country code:  "))
        try:
            phone1 = phonenumbers.parse(phone)
            print(geocoder.description_for_number(phone1, "en"), carrier.name_for_number(phone1, "en"),
                  timezone.time_zones_for_number(phone1))
            signup.phone = phone
        except:
            print("Invalid Number")
        usern=input("Please Enter your Email adress here: ")
        if (re.search(regex, usern)):
            try:
                signup.email=usern
            except :
                print("Please provide a valid emial address!")

        pas=input("Enter your password here: ")
        flag = 0
        while True:  
            if (len(pas)<8):
                flag = -1
                break
            elif not re.search("[a-z]", pas):
                flag = -1
                break
            elif not re.search("[A-Z]", pas):
                flag = -1
                break
            elif not re.search("[0-9]", pas):
                flag = -1
                break
            elif not re.search("[_@$]", pas):
                flag = -1
                break
            elif re.search("\s", pas):
                flag = -1
                break
            else:
                flag = 0
                signup.password=pas
                break
            
        if flag ==-1:
            
                print("The Password need 8 cherters\ninclude capital latter\nsmall later\nnumber\/ and one spacial cherecter '_''@''$' ")

        if signup.email and signup.password !=Null:
            try:
                
                auth.create_user_with_email_and_password(signup.email, signup.password)
                signup.employee_id=uuid4().int & (1<<16)-1
                try:
                    data={'UserID: ' : signup.employee_id, 
                          'User Name: ' : ((signup.first_name +' '+ signup.last_name)) }
                    insert=("insert into Employee_info (name,id,email,phone) values ('"+ fname  +"','"+ str(signup.employee_id)  +"','"+ str(usern)  +"','"+ str(phone)  +"')")

                    mycursor.execute(insert)
                    mydb.commit()
                except:
                    print("Invalid Entry")
                print("Hurry!\nSucessfull Created Your Account...") 
            except :
                print("UnsucessFull Signup") 
                
    def save(self):
        signup.user_data={'EmployeeID: ' : signup.employee_id, '\n'
                          'User Name: ' : signup.email,'\n'
                          'Password: '  : signup.password}

        print(signup.user_data)
        print("Manager Added Sucessfully")
        


def main():
    s=signup()
    s.signup()

main()