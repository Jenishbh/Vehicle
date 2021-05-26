import phonenumbers
#from Signup import signup
import re, random
from pyasn1.type.univ import Null
from pyrebase import pyrebase
from uuid import uuid4
from phonenumbers import geocoder, carrier, timezone

import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='vehicle'

)

mycursor=mydb.cursor()
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

Config = {
    'apiKey': "AIzaSyBzQAkYoCObHSDUrKVZq-ZNYh3tARqKSbE",
    'authDomain': "vehicle-user-log-in.firebaseapp.com",
    'databaseURL': "https://vehicle-user-log-in-default-rtdb.firebaseio.com",
    'projectId': "vehicle-user-log-in",
    'storageBucket': "vehicle-user-log-in.appspot.com",
    'messagingSenderId': "806241010296",
    'appId': "1:806241010296:web:1e4b372fd8a6683984638d",
    'measurementId': "G-4BP8G714Z8"
}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()


class Employee():
    def __init__(self):
        Employee.first_name = ()
        Employee.last_name = ()
        Employee.phone = ()
        Employee.employee_id = ()
        Employee.email = ()
        Employee.password = ()
        Employee.employee_status = bool(False)
        Employee.Employee_list = ()
        Employee.Work_assign = ()

    @staticmethod
    def signup():
        fname = input("Please Enter Employee's First Name Here: ")
        if type(fname) == str:
            try:
                Employee.first_name = fname
            except:
                print("Please Enter Employee name only")
        lname = input("Please Enter Employee Last name Here: ")
        if type(lname) == str and lname != fname:
            try:
                Employee.last_name = lname
            except:
                print("Please Enter Employee Last name only")
        phone = (input("Please Enter a Phone Number along Country code:  "))
        try:
            phone1 = phonenumbers.parse(phone)
            print(geocoder.description_for_number(phone1, "en"), carrier.name_for_number(phone1, "en"),
                  timezone.time_zones_for_number(phone1))
            Employee.phone = phone
        except:
            print("Invalid Number")
        usern = input("Please Enter Employee Email adress here: ")
        if (re.search(regex, usern)):
            try:
                Employee.email = usern
            except:
                print("Please provide a valid emial address!")

        pas = input("Please Create a Employee password here: ")
        flag = 0
        while True:
            if (len(pas) < 8):
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
                Employee.password = pas
                break

        if flag == -1:
            print(
                "The Password need 8 cherters\ninclude capital latter\nsmall later\nnumber\/ and one spacial cherecter '_''@''$' ")

        if Employee.email and Employee.password != Null:
            try:

                auth.create_user_with_email_and_password(Employee.email, Employee.password)
                Employee.employee_id = uuid4().int & (1 << 16) - 1
                try:
                    data = {'UserID: ': Employee.employee_id,
                            'User Name: ': ((Employee.first_name + ' ' + Employee.last_name)),
                            'Employee status': 'Inactive'}
                    a=('Inactive')
                    insert=("insert into employee_info (name,id,email,phone,status) values ('"+ fname  +"','"+ str(Employee.employee_id)  +"','"+ str(usern)  +"','"+ str(phone)  +"','"+ a  +"')")

                    mycursor.execute(insert)
                    mydb.commit()
                except:
                    print("Invalid Entry")
                print("Hurry!\nSuccessfully Created Your Account...\n Please Noted: Your User Id is: "+str(Employee.employee_id))
            except:
                print("Unsuccessfully Signup")

    @staticmethod
    def save():
        Employee.user_data = {'EmployeeID: ': Employee.employee_id,
                              'Phone Number: ': Employee.phone, '\n'
                              'User Name: ': Employee.email, '\n'
                              'Password: ': Employee.password}

        print(Employee.user_data)
        print("Manager Added Successfully")

    def login(self):
        while True:
            e = input("Email: ")
            p = input("Password: ")
            if e and p != Null:
                try:
                    auth.sign_in_with_email_and_password(e, p)
                    try:
                        print("You are successfully Login")
                        break
                    except:
                        print("Please Enter Correct Username and password")
                except:
                    print("Please Enter Correct Username and password")
            else:
                print("Please Enter valid Email And password")

    def work_assign(self):
        user=int(input("5 digit User ID: "))
        find=("select id from user_info where id = ('"+ str(user)  +"')" )
        mycursor.execute(find)
        for i in mycursor:
            
                try:
                    a=("select * from employee_info where id=('"+ str(user)  +"')")
                    mycursor.execute(a)
                    print(mycursor)
                    
                except:
                    print("Employee dosen't Exist")

    def employee_status(self):
        db.child('Employee').child(Employee.employee_id).child('Employee status').get()

    def employee_list(self):
        a = db.child('Employee').get()
        print(a)

    def employee_record(self):
        p = input('Please Enter an Employee Id')
        if p in db.child('Employee').shallow().get().val():
            print(p)





def main():
    s = Employee()
    s.signup()
    s.login()



main()