

import pandas as pd
import mysql.connector as connection

mydb=connection.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='vehicle'

)

mycursor=mydb.cursor()

class database():

    def add_part(self):
       
        id=int(input("Enetr part Id: "))
        name=(input("Enter Part name: "))
        price=int(input("enter part Price: "))
        labour=int(input("Enter labour charge: "))
        total= price + labour
        add=("insert into databas (part_id, part_name, part_price, labour_charge, total) values ('"+ str(id)  +"','"+ name  +"','"+ str(price)  +"','"+ str(labour)  +"','"+ str(total)  +"')")
        mycursor.execute(add)
        mydb.commit()

    def search_part(self):

        id=int(input("Please Enter part ID: "))
        find=("select part_id, part_name, total from database where part_id = '"+ str(id)  +"'")
        mycursor.execute(find)
        a=pd.read_sql(find,mydb)
        print(a)


def main():
    s=database()
    s.add_part()

main()

