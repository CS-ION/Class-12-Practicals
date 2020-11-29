ID = ['ABC','DEF','GHI']  #list containing the bike ID's in string
OUT = [9.55,10.11,10.23]  #list containing the time the bike was taken in float

def add_bike():
    bikeId = input("Enter bikeID ")
    if bikeId == 'ZZZ':
        print('Goodbye, Have a nice day')
        raise SystemExit
    ID.append(bikeId)
    OUT.append(float(input("Enter the time ")))
    return f'Bike {bikeId} added'
    
def bike():
    Id = input('enter bikeID : ')
    if Id not in ID:
        return 'Error, BIKEID NOT FOUND'
    OUT_time = OUT[ID.index(Id)]
    curr_time = float(input('enter the current time : '))
    return f'Time difference : {curr_time - OUT_time}'

while True:
    choice = input('1. Do you want to add bikes or \n2. Search Bikes (1/2) : ')
    if choice == '1':
        print(add_bike())
    elif choice == '2':
        print(bike())
