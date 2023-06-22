stack=[]
def push():
    n=int(input('Enter the How many element need to add:'))
    for i in range(0,n):
        key=int(input('Enter the Element :'))
        stack.append(key)
    print('Inserted Sucessfully')
    print(stack)
def pop():
    stack.pop()
    print('Deleted Sucessfully')
    print(stack)  
    
def display():
    print('Stack Elements')
    print(stack)
        
def peek():
    if len(stack) == 0:
        print('Stack is Empty')
    else:
        print(stack[-1])              

while 1:
    print('--Stack Operations --\n')
    print('1.PUSH\n2.POP\n3.DISPLAY\n4.PEEK\n5.QUIT')
    ch=int(input('Enter the Choice: '))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        display()
    elif ch==4:
        peek()
    elif ch==5:
        break
    else:
        print('Please enter the correct option!')
        
        