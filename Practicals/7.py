def binary_search(L, high , low , x):
    if high < low :
        return None
    mid = ( high + low )//2
    if L[mid]>x :
        return binary_search(L, mid-1 , low , x)
    elif L[mid]<x :
        return binary_search(L, high , mid+1 , x)
    else:
        return mid

L = [int(input('enter element : ')) for I in range(int(input('enter the size : '))) ]
item = int(input('enter the item to be searched : '))
result = binary_search(L, len(L)-1 , 0 ,item)
if result == None:
    print('item not found')
print('element found at index position',result)
