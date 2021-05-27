




import mysql.connector
import pandas as pd
from pyasn1.type.univ import Null

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='vehicle'

)

mycursor=mydb.cursor()

class repair():
    def __init__(self,id):
        self.id=id

    def repair_list(self):
        
        i=("select * from car_info where i = '"+ str(self.id)  +"'")
        mycursor.execute(i)
        a=pd.read_sql(i,mydb)
        print(a)
        a=("insert into status(id) values = '"+ str(self.id)  +"'")

    def car_repair(self):
        status=input("Enter a decscription: ")
        a=("update status Set Status = '"+ status  +"' ")
        mycursor.execute(a)

    def search_part(self):

        id=int(input("Please Enter part ID: "))
        find=("select part_id, part_name,total from databas where part_id = '"+ str(id)  +"'")
        mycursor.execute(find)
        b=mycursor.fetchall()
        a=pd.DataFrame(b)
        print(a)
        if a != Null:
            while True:
                ask=input("If you want to add part?\n")
                if ask != Null:

                        if ask == 'yes' or 'YES' or 'Yes':

                            add= "update status set  price = price + (select price from databas where partr_id = id ) where id = self.id "
                            mycursor.execute(add)

                        elif ask == 'no' or 'NO' or 'No':
                            print("Ok")
                            break
                        else:
                            print("Please Only Enter Yes or No ")
                else:
                    print("Please enter Yes or No")
        else:
            print("Part is Not found")





        

def main():
    s=repair(214)
    s.search_part()
main()





    






















































