

from pyasn1.type.univ import Null
from pyrebase import pyrebase
import firebase_admin
from firebase_admin import credentials,db
#cred = credentials.Certificate("serviceAccountKey.json")
import pandas as pd
import mysql.connector as connection

mydb=connection.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='vehicle'

)

mycursor=mydb.cursor()



#firebase_admin.initialize_app(cred, {
#    'databaseURL': "https://user-side-59131-default-rtdb.firebaseio.com/"
#})
#Config = {
#  "apiKey": "AIzaSyBzQAkYoCObHSDUrKVZq-ZNYh3tARqKSbE",
#  "authDomain": "vehicle-user-log-in.firebaseapp.com",
#  "databaseURL": "https://vehicle-user-log-in-default-rtdb.firebaseio.com",
#  "projectId": "vehicle-user-log-in",
#  "storageBucket": "vehicle-user-log-in.appspot.com",
#  "messagingSenderId": "806241010296",
#  "appId": "1:806241010296:web:1e4b372fd8a6683984638d",
#  "measurementId": "G-4BP8G714Z8"
#}
#
#
#
#Config_user={
#    "apiKey": "AIzaSyDXCFGuraREwDJPBbULmqLxH99cO_6egXY",
#    "authDomain": "user-side-59131.firebaseapp.com",
#    "databaseURL": "https://user-side-59131-default-rtdb.firebaseio.com/",
#    "projectId": "user-side-59131",
#    "storageBucket": "user-side-59131.appspot.com",
#    "messagingSenderId": "790675146359",
#    "appId": "1:790675146359:web:c253dbfeafa0db8d796872",
#    "measurementId": "G-9J4VGRBWFD"
#}
#
#firebase=pyrebase.initialize_app(Config)
#
#firebase_user=pyrebase.initialize_app(Config_user)
#
#db1=firebase.database()
#
#db_user=firebase.database()




class booked():
    def __init__(self):
        pass



    def book_list(self):
        find=("select booking_user.id, name, email, phone, car_make, car_model,car_year, date, time from booking_user, user_info, car_info where booking_status = 'Panding' and booking_user.id=user_info.id and booking_user.id=car_info.id")

        
        a=pd.read_sql(find,mydb)
        print(a)
        
    def emoplyee_list(self):
        
        find=("SELECT * FROM employee_info where status = 'Active'")
        a=pd.read_sql(find,mydb)
        print(a)

    def assign_work(self):

        user=int(input("Please Enter User ID: "))
        employee=int(input("Please Enter Employee ID: "))

        insert=("update car_info set assign_employee_id = (select id from employee_info where id=('"+ str(employee)  +"') where id='"+ str(user)  +"'; update car_info set assign_employee_phone = (select phone from employee_info where id='"+ str(employee)  +"') where id='"+ str(user)  +"'")
        mycursor.execute(insert)
        a=("update booking_user set booking_status = 'Accepted' where id='"+ str(user)  +"'")
        mycursor.execute(a)
        b=("update employee_info set status = 'Active' where id = '"+ str(employee)  +"'")
        mycursor.execute(b)
        print("The Employee: %d is assigned to the User: %d",(employee,user))
        


    def decline(self):
        user=int(input("Please Enter User ID: "))
        a=("update booking_user set booking_status = 'Declined' where id='"+ str(user)  +"'")
        reason=input("Please Enter your reason  declining the booking: ")
        mycursor.execute(a)


        print("Your Application Was rejected\n the reason: ",reason)

    
        


def main():
    s=booked()
    s.book_list()
#

main()