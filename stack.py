stack=[]
def push():
    if len(stack)==n:
        print("stack is full!")
    element=input("enter the value: ")
    stack.append(element)
    print(stack)

def pop():
    if (len(stack))==0:
        print("the stack is empty!")
    else:
       e=stack.pop()
       print("remove element",e)
       print(stack)
n=int(input("enter the length of the stack: "))
while True:
    print("enter the choice if 1.push, 2.pop, 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("enter the correct operation")               

