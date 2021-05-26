from pyasn1.type.univ import Null
from pyrebase import pyrebase
import  datetime
#from Log_in import Signup
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='vehicle'

)

mycursor=mydb.cursor()



Config={
    "apiKey": "AIzaSyDXCFGuraREwDJPBbULmqLxH99cO_6egXY",
    "authDomain": "user-side-59131.firebaseapp.com",
    "databaseURL": "https://user-side-59131-default-rtdb.firebaseio.com/",
    "projectId": "user-side-59131",
    "storageBucket": "user-side-59131.appspot.com",
    "messagingSenderId": "790675146359",
    "appId": "1:790675146359:web:c253dbfeafa0db8d796872",
    "measurementId": "G-9J4VGRBWFD"
}

firebase=pyrebase.initialize_app(Config)
db=firebase.database()




class Booking():
    def __init__(self):
        Booking.time=[]
        Booking.date=[]
        Booking.details={}
        

    def book(self):
        user=(input("5 digit User ID: "))
        find=("select id from user_info where id = ('"+ str(user)  +"')" )
        mycursor.execute(find)
        for i in mycursor:
                print(i)
                date_entry = input('Enter a date in YYYY-MM-DD format')
                year, month, day = map(int, date_entry.split('-'))
                print({'Date: ':str(datetime.date(year, month, day))})
                
                time_entry = input('Enter a Time in HH:MM:SS format')
                Hour, Minutes, Seconds = map(int, time_entry.split(':'))
                print({'Time: ':str(datetime.time(Hour, Minutes, Seconds))})
                
                a=("Panding")
                try:
                    insert=("insert into booking_user (id, date, time, booking_status) values ('"+ str(user)  +"','"+ str(datetime.date(year, month, day)) +"','"+ str(datetime.time(Hour, Minutes, Seconds))  +"','"+ a  +"')")
                    mycursor.execute(insert)
                    mydb.commit()
                    print("Booking is Padding")
                except ValueError:
                    print("Incorrect Entry")
                

    

def main():
    s=Booking()
    s.book()

main()