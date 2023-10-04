
def sum():
    a=(int(input("enter the number: ")))
    b=(int(input("enter the number: ")))
    c=(a+b)
    print(str(a) + "+" + str(b) +"="+ str(c))

def sub():
    a=(int(input("enter the number: ")))
    b=(int(input("enter the input number: ")))
    c=(a-b)
    print(str(a) +"-"+ str(b) + "="+ str(c))

def division():
    a=(int(input("enter the input number: ")))
    b=(int(input("enter the input number: "))) 
    c=(a/b)
    print(str(a) + "/" + str(b) + "=" + str(c))
def multiplicastion():
    a=(int(input("enter the input number: ")))
    b=(int(input("enter the input number: ")))
    c=(a*b) 
    print(str(a) + "*"+str(b)+ "="+ str(c))   
while True:
    print("enter your choice if 1.addition 2.subtraction 3.division 4.muitiplication 5.quit")
    choice=(int(input("enter you choice: ")))
    if choice ==1:
        sum()
    elif choice ==2:
        sub()
    elif choice == 3:
        division()
    elif choice ==4:
        multiplicastion()
    elif choice ==5:   
        break
    else:
        print("enter the correct choice! ")           
  