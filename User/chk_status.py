
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
        f=("select * from status where id='"+ str(id)  +"'" )
        mycursor.execute(f)
        
        for a in mycursor.fetchall():
            print (a)



def main():
    s=chk_status()
    s.chk(54720)

main()