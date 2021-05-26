import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='vehicle'

)

mycursor=mydb.cursor()


user=int(input('enter: '))
car_made=input("enter: ")
car_model=(input(("enter: ")))

car_year=int(input("Enter: "))




add=("insert into car_info (id,car_make,car_model,car_year) values ('"+ str(user)  +"','"+ car_made  +"','"+ car_model  +"','"+ str(car_year)  +"')")
mycursor.execute(add)
mydb.commit()
for i in mycursor:
                        print(i)