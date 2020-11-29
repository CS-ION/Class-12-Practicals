import mysql.connector
#to check whether its connected
mydb=mysql.connector.connect(host='localhost',user='root',password='isgsql')
if mydb.is_connected()==False:
    print('not connected')
    raise SystemExit

#creating a cursor object
mycursor=mydb.cursor()

#using/creating database
try:
    mycursor.execute('create database Employee')
    mycursor.execute('use Employee')
except:
    mycursor.execute('use Employee')

def Insert_Initial():
    try:
        mycursor.execute('''create table Emp(Empno int primary key,
                         Empname varchar(30),
                         Salary int,
                         Department varchar(30),
                         Designation varchar(30))''')
    except:
        return #as table already exists
    rec_list = []
    for I in range(6):
        no=int(input('Enter employee no : '))
        name=input('Enter employee name : ')
        salary=float(input('Enter employee salary : '))
        department=input('Enter name of department : ')
        designation=input("Enter designation : ")
        rec_tuple=(no,name,salary,department,designation)
        rec_list.append(rec_tuple)
    command='insert into emp(empno,empname,salary,department,designation) values(%s,%s,%s,%s,%s)'
    mycursor.executemany(command,rec_list)
    print(mycursor.rowcount,'rows affected')
    mydb.commit()
Insert_Initial()

#menu-driven functions

def addrecord():
    record = (
    int(input('Enter employee no : ')),
    input('Enter employee name : '),
    float(input('Enter employee salary : ')),
    input('Enter name of department : '),
    input("Enter designation : ") 
    )
    command='insert into emp values(%s,%s,%s,%s,%s)'
    mycursor.execute(command,record)
    mydb.commit()
    print('Operation successfull : record added')
    
def searchrecord():
    try:
        query = (
        int(input('Enter Employee no : ')),
        input('Enter dept : ')
        )
        command='select * from emp where Empno=%s and department=%s'
        mycursor.execute(command,query)
        records=mycursor.fetchall()
        for I in records:
            print(I)
    except:
        print('Record not found')
  
def updaterecord():
    query = (input('Enter Department to be updated : '),input('Enter Designation to be updated : '))
    command='update emp set salary=salary+0.35*salary where Department=%s and Designation=%s'
    try:
        mycursor.execute(command,query)
        mydb.commit()
        print('Record updated')
    except:
        print('Record not found')

def deleterecord():
    query = (input('Enter Department'),)
    command='delete from emp where Department=%s and Salary<15000'
    try:
        mycursor.execute(command,query)
        mydb.commit()
        print('Record deleted')
    except:
        print('Record not found')

def display():
    mycursor.execute('select * from emp')
    for I in mycursor.fetchall():
        print(I)

#menu-driven
print('''MENU
1. Add record
2. Search record
3. Update record
4. Delete record
5. Display Records
Press any other key to exit\n''')
while True:
    ch=input('Enter your choice :')
    if ch=='1':
        addrecord()
    elif ch=='2':
        searchrecord()
    elif ch=='3':
        updaterecord()
    elif ch=='4':
        deleterecord()
    elif ch=='5':
        display()
    else:
        raise SystemExit
