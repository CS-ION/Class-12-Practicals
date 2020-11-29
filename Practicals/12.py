def file_upper(f):
    count = 0 
    for I in f.readlines():
        for J in I.split(' '):
            if J[0].isupper():
                count += 1
    return f'No of words starting with uppercasees : {count}'
filename = open('coordinates.txt','r')
print(file_upper(filename))
