stack = [int(input('Enter the elements')) for I in range(int(input('Enter size ')))]
temp = []
for I in range(len(stack)):
    val = stack.pop()
    if val % 2 != 0 :
        temp.append(val)
for I in temp:
    stack.append(I)
print(stack)
