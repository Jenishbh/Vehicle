import re
from uuid import uuid4
from pyasn1.type.univ import Null
from pyrebase import pyrebase
from datetime import datetime
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

Confif={
    "apiKey": "AIzaSyDXCFGuraREwDJPBbULmqLxH99cO_6egXY",
    "authDomain": "user-side-59131.firebaseapp.com",
    "databaseURL": "https://user-side-59131-default-rtdb.firebaseio.com/",
    "projectId": "user-side-59131",
    "storageBucket": "user-side-59131.appspot.com",
    "messagingSenderId": "790675146359",
    "appId": "1:790675146359:web:c253dbfeafa0db8d796872",
    "measurementId": "G-9J4VGRBWFD"
}

firebase=pyrebase.initialize_app(Confif)
auth=firebase.auth()
db=firebase.database()

class Signup():
    def __init__(self):
        Signup.email=()
        Signup.password=()
        Signup.first_name=()
        Signup.last_name=()
        Signup.user_data={}
        Signup.userid=()
        Signup.phone=()




    def signup(self):
        fname=input("Please Enter Your First Name Here: ")
        if type(fname)==str:
            try:
                Signup.first_name=fname
            except:
                print("Please Enter Your name only")
        lname=input("Please Enter Your Last name Here: ")
        if type(lname)==str and lname!=fname:
            try:
                Signup.last_name=lname
            except :
                print("Please Enter Your Last name only")
        phone = (input("Please Enter a Phone Number along Country code:  "))
        try:
            phone1 = phonenumbers.parse(phone)
            print(geocoder.description_for_number(phone1, "en"), carrier.name_for_number(phone1, "en"),
                  timezone.time_zones_for_number(phone1))
            Signup.phone = phone
        except:
            print("Invalid Number")
        usern=input("Please Enter your Email adress here: ")
        if (re.search(regex, usern)):
            try:
                Signup.email=usern
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
                Signup.password=pas
                break
            
        if flag ==-1:
            
                print("The Password need 8 cherters\ninclude capital latter\nsmall later\nnumber\/ and one spacial cherecter '_''@''$' ")

        if Signup.email and Signup.password !=Null:
            try:
                
                auth.create_user_with_email_and_password(Signup.email, Signup.password)
                Signup.userid=uuid4().int & (1<<16)-1
                try:
                    data={'UserID: ' : Signup.userid, 
                          'User Name: ' : ((Signup.first_name +' '+ Signup.last_name)) }
                    insert=("insert into User_info (name,id,email,phone) values ('"+ fname  +"','"+ str(Signup.userid)  +"','"+ str(usern)  +"','"+ str(phone)  +"')")

                    mycursor.execute(insert)
                    mydb.commit()
                except:
                    print("Invalid Entry")
                    
                print("Hurry!\nSuccessfully Created Your Account...\n Your User Id is: "+str(Signup.userid))
            except :
                
                print("Unsuccessfully Signup")
                
    def save(self):
        Signup.user_data={'UserID: ' : Signup.userid, '\n'
                          'User Name: ' : Signup.email,'\n'
                          'Password: '  : Signup.password}

        print(Signup.user_data)
        print("User Added Sucessfully")
        
    #def pri(self):
    #    print("Your name: "+str(Signup.first_name)+" "+str(Signup.last_name)+"\n"+"Username: "+str(Signup.email)+"\n"+"And Your passowerd: "+str(Signup.password))












class Login():
    def __init__(self):
        pass


    
    def login(self):
            i=1
            s=0
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
                            print("Ouch! I'm Sorry it's not your problem it's our server problem we are working on it... ")
                    except:
                        if i!=3:
                            print("Please Enter Correct Username and password")
                            
                            i+=1
                        else:
                            print("Sorry You are out of your chance please come back for login again")
                            s=1
                            break
                else:
                        print("Please Enter valid Email And password")
                        return 'unsuccessful'
    
    

































