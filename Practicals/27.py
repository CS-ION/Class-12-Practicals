D={input('Enter friends name : '):int(input('Enter friends ph no : ')) for I in range(int(input('Enter total no of friends : '))) }

def display(d):
    for I in d.items():
        print(I[0],I[1])

def add(d):
    d[input('Enter friends name : ')] = int(input('Enter friends ph no : '))

def delete(d):
    del d[input('Enter friends name whos details have to be deleted : ')]

def modify(d):
    d[input('Enter friends name : ')] = int(input('Enter friends ph no : '))

def check(d):
    name = input('Enter friends name to be checked : ')
    if name in d.keys():
        print(name,d[name])

def disp_sort(d):
    for I in sorted(d.items()):
        print(I[0],I[1])

print('''CHOOSE THE FOLLOWING OPTIONS
1. Display the name and phone number of all your
friends
2. Add a new key-value pair in this dictionary and
display the modified dictionary
3. Delete a particular friend from the dictionary
4. Modify the phone number of an existing friend
5. Check if a friend is present in the dictionary or
not
6. Display the dictionary in sorted order of names
PRESS ANY OTHER KEY TO EXIT''')

while True:
    choice = input('Enter the option number :')
    if choice == '1':
        display(D)
    elif choice == '2':
        add(D)
        print('OPERATION DONE SUCCESSFULLY')
    elif choice == '3':
        delete(D)
        print('OPERATION DONE SUCCESSFULLY')
    elif choice == '4':
        modify(D)
        print('OPERATION DONE SUCCESSFULLY')
    elif choice == '5':
        check(D)
    elif choice == '6':
        disp_sort(D)
    else:
        raise SystemExit
    


