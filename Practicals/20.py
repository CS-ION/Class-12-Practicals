print('''Various Array Operations
1. Linear Search
2. Binary Search
3. Lowest Number 
4. Selection Sort
Press any other key to exit''')

def create_array():
    L = [int(input('Enter element ')) for I in range(int(input('Enter size ')))]
    print(L)
    return L

def low(L):
    print(f'Lowest no : {min(L)}')

def lin_search(L):
    x = int(input('Enter element to be searched : '))
    for I in range(len(L)):
        if L[I] == x:
            print('Element found at index position :',I)
            return
    print('Element not found')

def binary_search(L, high , low , x):
    L = sel_sort(L)
    if high < low :
        return 'Element not found'
    mid = ( high + low )//2
    if L[mid]>x :
        return binary_search(L, mid-1 , low , x)
    elif L[mid]<x :
        return binary_search(L, high , mid+1 , x)
    else:
        return f'Element found at index position (in the sorted array{L}) at {mid}'

def sel_sort(L):
    for i in range(len(L)): 
        min_idx = i 
        for j in range(i+1, len(L)): 
            if L[min_idx] > L[j]: 
                min_idx = j        
        L[i], L[min_idx] = L[min_idx], L[i] 
    return L

L =  create_array()
while True:
    choice = input('Enter choice : ')
    if choice == '1':
        lin_search(L)
    elif choice == '2':
        x = int(input('Enter element to be searched : '))
        print(binary_search(L, len(L)-1 , 0 ,x))
    elif choice == '3':
        low(L)
    elif choice == '4':
        print(f'Sorted Array : {sel_sort(L)}')
    else:
        raise SystemExit
