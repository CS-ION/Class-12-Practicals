report = ()
mark = ()

for I in range(3):
    name = input('Enter name :') 
    marks = int(input('Enter the marks'))
    mark += (marks,)
    report += ((name,marks),)

below_33 = 0
above_60 = 0

for I in report:
    if I[1]>60:
        above_60 += 1
    elif I[1]<33:
        below_33 += 1
    if I[1] == max(mark):
        print(f'Highest marks : {I}')
    elif I[1] == min(mark):
        print(f'Lowest marks : {I}')

print(f'Students below 33 : {below_33}')
print(f'Students above 60 : {above_60}')
