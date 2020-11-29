VIP = [111]
Balcony = [222]
Regular = [333]

def insert(tokenId,priority):
    if priority.upper() == 'H':
        VIP.append(tokenId)
    elif priority.upper() == 'N':
        Balcony.append(tokenId)
    elif priority.upper() == 'L':
        Regular.append(tokenId)
    print('Operation Successful')

def search(t):
    if (t not in VIP) and (t not in Balcony) and (t not in Regular):
        print('invalid token')
        return
    if t in VIP:
        print('tokenID found in highest priority (VIP)')
    elif t in Balcony:
        print('tokenID found in normal priority (Balcony)')
    elif t in Regular:
        print('tokenID found in lowest priority (Regular)')

def change(t,p):
    if (t not in VIP) and (t not in Balcony) and (t not in Regular):
        print('invalid token')
        return
    if t in VIP:
        VIP.remove(t)
    elif t in Balcony:
        Balcony.remove(t)
    elif t in Regular:
        Regular.remove(t)
    insert(t,p)

def display():
    print(VIP)
    print(Balcony)
    print(Regular)

print('''CHOOSE THE FOLLOWING OPERATIONS
1. Insert tokenId
2. Search for an Id
3. Change Priority
4. Display''')

while True:
    choice = input('Enter choice : ')
    if choice == '1':
        tokenId = int(input('Enter tokenId : '))
        priority = input('Priority(Highest/Normal/lowest(H/N/L): ')
        insert(tokenId,priority)
    elif choice == '2':
        token = int(input('Enter tokenId : '))
        search(token)
    elif choice == '3':
        token = int(input('Enter tokenId : '))
        priority = input('Priority(Highest/Normal/lowest(H/N/L): ')
        change(token,priority)
    elif choice == '4':
        display()
    else:
        raise SystemExit
    
