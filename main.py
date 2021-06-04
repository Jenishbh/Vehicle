

def add():
    a=float(input("enetr a main balance: "))
    b=float(input("enter a deduction: "))
    p=0
    while True:
        
        print("Attempt: ",p)
        p+=1
        if a>=b:
            print("Amount paid: ",b)
            a-=b
            
            
            print("remaining  amount: ",round(a,2))
        elif a!=0:
            print("Amount paid: ",round(a,2))
            
            a-=a
            
            print("remening amount: ",round(a,2))
        else:
            print("you have 0 amount")
            break

            


add()