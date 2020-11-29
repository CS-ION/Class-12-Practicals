import pickle

def initial():
    try:
        f = open('roman.txt','wb')
    except:
        return
    D = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X'}
    pickle.dump(D,f)

def read(file,n):
    try:
        while True:
            D = pickle.load(file)
            try:
                print(f"Roman equivalent for {n} : {D[n]}")
            except:
                print('Your number might be out of range. Pls choose bw 1 and 10')
                return
    except EOFError:
        return
    
initial()
while True:
    no = input('Enter the no : ')
    if no == '-1':
        raise SystemExit
    else:
        read(open('roman.txt','rb'),int(no))
