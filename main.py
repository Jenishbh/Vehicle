
from User.Log_in import Login
from User.Log_in import Signup



def main():
    aa=Login()
    c=Signup()
    end=1
    while end==1:
        a=input(("Please enter one of the following choices: \n1.Login\n2.Signup\n3.Exit\n"))
        log='1' or 'Login'
        sig='2' or 'Signup'
        exi= '3' or 'Exit'
        try:
            if a == log:

                aa.login()
                
            elif a == sig:

                c.signup()
            elif a == exi:
                print("Thank you for visiting us!\nSee you soon\nBye!")
                raise Exception
            else:
                print("Thank you for visiting us!\nSee you soon\nBye!")
                raise Exception
        except Exception:
            end=0
        
        
        

main()



























#def add():
#    a=float(input("enetr a main balance: "))
#    b=float(input("enter a deduction: "))
#    p=0
#    while True:
#        
#        print("Attempt: ",p)
#        p+=1
#        if a>=b:
#            print("Amount paid: ",b)
#            a-=b
#            
#            
#            print("remaining  amount: ",round(a,2))
#        elif a!=0:
#            print("Amount paid: ",round(a,2))
#            
#            a-=a
#            
#            print("remening amount: ",round(a,2))
#        else:
#            print("you have 0 amount")
#            break
#
#            
#
#
#add()