L = []
n = int(input('enter the number : '))
while n>0:
    L.append(str(n))
    n = n-5 
print(' '.join(L),str(n),' '.join(L[::-1]))