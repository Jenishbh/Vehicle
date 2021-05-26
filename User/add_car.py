import re, random
from pyasn1.type.univ import Null
from pyrebase import pyrebase
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

class add_car():
    def __init__(self):
        add_car.car_made=()
        add_car.car_model=()
        add_car.car_year=()



    def add_car(self):
        user=int(input("5 digit User ID: "))
        find=("select id from user_info where id = ('"+ str(user)  +"')" )
        mycursor.execute(find)
        for i in mycursor:
            print(i)
         
        
            car_made=input("Car Company: ")
            car_model=input("Car Model: ")
            car_year=int(input("Car Year: "))
        

            if car_model and car_year and car_made != Null:

                

                try:
                    data={'Car Comapny: ' : add_car.car_made,
                          'Car Model: ' : add_car.car_model,
                          'Car Manufacture Year: ' : add_car.car_year}
                    add=("insert into car_info (id,car_make,car_model,car_year) values ('"+ str(user)  +"','"+ car_made  +"','"+ car_model  +"','"+ str(car_year)  +"')")
                    mycursor.execute(add)
                    mydb.commit()
                    for i in mycursor:
                        print(i)
                    print("sucessfull enter the Data")
                    break
                    

                except:
                    print('Database error')

         
        print('Invalid Data Entry')
        #else:
        #    while True:
        #        user=(input("5 digit User ID: "))
        #        if user != Null:
        #            try:
        #                find=("select * from user_info where id = ('"+ str(user)  +"')" )
        #            except:
        #                print("Please enter correct user Id")




def main():
    s=add_car()
    s.add_car()

main()



