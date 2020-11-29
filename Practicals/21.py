QUEUE = [(1122,'Ayaan Jilani',24)]
#of the form MemberNo(integer) , MemberName(String),Age(integer)

def insert(QUEUE):
    x = (int(input('Enter employee no : ')),
    input('Enter employee name : '),
    int(input('Enter age : ')))
    QUEUE.append(x)

def delete(QUEUE):
    if QUEUE == []:
        print('Underflow alert')
        return
    popped = QUEUE.pop(0)
    print('Empl0yee removed :',popped)

def display(QUEUE):
    print(QUEUE)

print('''CHOOSE YOUR OPERATION BY TYPING THE NUMBER
    1. INSERT INTO QUEUE
    2. DELETE FROM QUEUE
    3. DISPLAY QUEUE
    Press any other key to exit''')

while True:
    choice = input('Enter choice : ')
    if choice == '1':
        insert(QUEUE)
    elif choice == '2':
        delete(QUEUE)
    elif choice == '3':
        display(QUEUE)
    else:
        raise SystemExit
    
