import os 
f = open('text.txt','r')
stack = []
for I in f.readlines():
    stack.append(I)
f.close()
os.remove('text.txt')
f = open('text.txt','w')
for I in range(len(stack)):
    f.write(stack.pop())
f.close()
