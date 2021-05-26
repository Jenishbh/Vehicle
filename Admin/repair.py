
from data import *



import mysql.connector
import pandas as pd
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='vehicle'

)

mycursor=mydb.cursor()
class repair(database):
    def __init__(self):
        pass

    def repair_list(self,id):
        
        i=("select * from car_info where i = '"+ str(id)  +"'")
        mycursor.execute(i)
        a=pd.read_sql(i,mydb)
        print(a)
        a=("insert into status(id) values = '"+ str(id)  +"'")

    def car_repair(self):
        status=input("Enter a decscription: ")
        a=("update status Set Status = '"+ status  +"' ")
        mycursor.execute(a)

    def search(self):
        a=database.search_part()
        print(a)
        



        

def main():
    s=repair()
    s.search()
main()





    






















































