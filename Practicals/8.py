def bubble_sort1(L, I = 0):
    J = I
    try: 
        if L[J]>L[J+1]:
            L[J],L[J+1]=L[J+1],L[J]
    except:
        return None
    return bubble_sort1(L, I = I+1)

L = [int(input('enter element : ')) for I in range(int(input('enter the size : '))) ]
for I in range(len(L)):
    bubble_sort1(L)
print('sorted : ',L)
