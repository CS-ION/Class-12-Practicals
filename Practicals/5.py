PLANE = ['AF333','LH543','BD566'] #planes to take off
DUE = [956,955,940] #due time of respective planes
CALL = [850,875,860] #time the planes were called in

def add_plane():
    PiD=input("enter the plane id:")
    if PiD=="ZZZ":
        print('no more planes waiting')
        raise SystemExit
    PLANE.append(PiD)
    DUE.append(int(input("enter take off time:")))
    CALL.append(int(input("enter calling time:")))
    return f'Plane {PiD} added'

def next_flight():
    plane,due,call = PLANE.pop(0),DUE.pop(0),CALL.pop(0)
    return f'''Next plane to take off : {plane}
Due time : {due}
Called time : {call}
No of planes left to take off : {len(PLANE)}'''
    
while True:
    choice = input('''1. Do you want to add planes
2. Is the runway free? (1/2) : ''')
    if choice == '2':
        print(next_flight())
    elif choice == '1':
        print(add_plane())
