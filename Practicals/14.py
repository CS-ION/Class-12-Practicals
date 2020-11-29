import pickle
import os

print('''MENU DRIVEN PROGRAM
1. Adding a new product (productid,productname, unitprice,quantity) - tuple
2. searching a product using productid
3. displaying the product details whose unitprice <10
4. delete the products whose quantity is <10
5. decrease the unitprice of the products by 3 whose quantity is >=10
ENTER YOUR CHOICE (1/2/3/4/5)''')

def add_product():
    f = open('product.pdf','wb')
    prod_id = int(input('enter product id : '))
    prod_name = input('enter product name : ')
    unit_price = float(input('enter unit price : '))
    quantity = float(input('enter quantity : '))
    T = (prod_id,prod_name,unit_price,quantity)
    pickle.dump(T,f)
    f.close()

def search():
    f = open('product.pdf','rb')
    ID = int(input('enter the product id : '))
    try:
        while True:
            T = pickle.load(f)
            if T[0] == ID:
                return T 
    except EOFError:
        return 'PRODUCT NOT FOUND'
    f.close()

def display():
    f = open('product.pdf','rb')
    try:
        while True:
            T = pickle.load(f)
            if T[2]<10:
                print(T) 
    except EOFError:
        f.close()

def delete():
    f = open('product.pdf','rb')
    f1 = open('temp.pdf','wb')
    try:
        while True:
            T = pickle.load(f)
            if T[3]<10:
                pickle.dump(T,f1) 
    except EOFError:
        f.close()
        f1.close()
    os.remove('product.pdf')
    os.rename('temp.pdf','product.pdf')

def decrease():
    f = open('product.pdf','rb')
    f1 = open('temp.pdf','wb')
    try:
        while True:
            T = pickle.load(f)
            if T[3]>10 or T[3]==10:
                T = (T[0],T[1],T[2]-3,T[3])
            pickle.dump(T,f1) 
    except EOFError:
        f.close()
        f1.close()
    os.remove('product.pdf')
    os.rename('temp.pdf','product.pdf')

while True:
    choice = input()
    if choice == '1':
        add_product()
        print('PRODUCT ADDED SUCCESSFULLY')
    elif choice == '2':
        x = search()
        print(x)
    elif choice == '3':
        display()
        print('If nothing was displayed it means there were no such products')
    elif choice == '4':
        delete()
        print('OPERATION DONE SUCCESSFULLY')
    elif choice == '5':
        decrease()
        print('OPERATION DONE SUCCESSFULLY')
    done = input('DO YOU WANT TO PERFORM MORE OPERATIONS? (Y/N) : ')
    if done.upper() == 'N':
        break




