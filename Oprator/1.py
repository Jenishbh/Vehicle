import mysql.connector
import  datetime
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='vehicle'

)

mycursor=mydb.cursor()

#mycursor.execute("create table User_info(name varchar(20), id int, email varchar(20), password varchar(20))")


id=int(input("Eneter Id: "))
date_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))

time_entry = input('Enter a Time in HH:MM:SS format')
Hour, Minutes, Seconds = map(int, time_entry.split(':'))

a=("Panding")

insert=("insert into booking_user (id, date, time, booking_status) values ('"+ str(id)  +"','"+ str(datetime.date(year, month, day)) +"','"+ str(datetime.time(Hour, Minutes, Seconds))  +"','"+ a  +"')")

mycursor.execute(insert)
mydb.commit()

#mycursor.execute('select * from User_info')
#
for i in mycursor:
    print(i)