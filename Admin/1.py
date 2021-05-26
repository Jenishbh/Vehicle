
import mysql.connector as connection

mydb=connection.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='vehicle'

)

mycursor=mydb.cursor()




b=int(input("enter"))
a=input("Enter")

add=("insert into databas (part_id, part_name) values ('"+ str(b)  +"','"+ str(a)  +"')")

mycursor.execute(add)
mydb.commit()




