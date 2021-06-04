
import mysql.connector as connection
import pandas as pd

mydb=connection.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='vehicle'

)

mycursor=mydb.cursor()



class chk_status():
    def chk(self,id):
        self.id=id
        f=("select * from status where id=self.id" )
        mycursor.execute(f)
        a=pd.read_sql(f,mydb)
        print(a)