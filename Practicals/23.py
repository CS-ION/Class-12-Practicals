print('''MENU DRIVEN PROGRAM
    1. ADD STUDENT
    2. DISPLAY STUDENT
    3. SEARCH STUDENT
    Press any other key to exit''')

def add_stud(file):
    roll_no = int(input('Enter the students roll no : '))
    name = input('Enter the name of the student : ')
    address = input('Enter the address of student : ')
    file.write(f"{roll_no} , {name} , {address}\n")

def disp_stud(file):
    for I in file.readlines():
        print(f'''Roll no : {I.split(',')[0]}
Name : {I.split(',')[1]}
Address : {I.split(',')[2]} ''')

def search_stud(file):
    search_no = input('Enter student roll no : ')
    for I in file.readlines():
        if search_no in I.split(',')[0]:
            print(f'''Roll no : {I.split(',')[0]}
            Name : {I.split(',')[1]}
            Address : {I.split(',')[2]} ''')
            return
    print('Student not found')

while True:
    choice = input('Enter choice : ')
    if choice == '1':
        add_stud(open('student.txt','a+'))
    elif choice == '2':
        disp_stud(open('student.txt','r'))
    elif choice == '3':
        search_stud(open('student.txt','r'))
    else:
        raise SystemExit


