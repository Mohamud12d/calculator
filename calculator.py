#------------------------------------------------------
#? Very important projects on the function
#-----------------------------------------------------
#--------------project one calculator app -------------
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
print("---------Welcome to simple calculator----------")
def menu():
    while True:
        print("1.add")
        print("2.subtract")
        print("3.multiply")
        print("4.--exit--")
        a=int(input("enter the number: "))
        b=int(input("enter the number: "))
        choice=int(input("choice: "))
        if choice==1:
            print(f"{a}+{b}={add(a,b)}")  
        elif choice==2:
            print(f"{a}-{b}={subtract(a,b)}")  
        elif choice==3:
            print(f"{a}*{b}={multiply(a,b)}")  
        elif choice==4:
            print("GOODBY")
            break
        else:
            print("invalid input")
menu()
