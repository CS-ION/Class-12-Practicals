stack = [('D145','WimpyKid',5000.0)]#stack of the form(Bookno,Bookname and Cost)
top = len(stack)

def push(stack):
    global top
    x = (input('Enter book no : '),
    input('Enter book name : '),
    float(input('Enter cost : ')))
    stack.append(x)
    top = len(stack)
    print('Length of the stack after push :',top)

def pop(stack):
    global top
    if stack == []:
        print('Underflow alert : length of stack is :',top)
        return
    stack.pop()
    top = len(stack)
    print('Length of the stack after pop :',top)

def display(stack):
    global top
    print(stack)
    print('Length of the stack:',top)

print('''CHOOSE YOUR OPERATION BY TYPING THE NUMBER
    1. PUSH INTO STACK
    2. POP FROM STACK
    3. DISPLAY STACK
    Press any other key to exit''')

while True:
    choice = input('Enter choice : ')
    if choice == '1':
        push(stack)
    elif choice == '2':
        pop(stack)
    elif choice == '3':
        display(stack)
    else:
        raise SystemExit
    
