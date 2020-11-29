import os
f = open('WORDS.txt','r')
f1 = open('temp.txt','w')
for line in f.readlines():
    line1 = ''
    for letter in line:
        if letter == 'J':
            letter = 'I'
        f1.write(letter)
f.close()
f1.close()
os.remove('WORDS.txt')
os.rename('temp.txt','WORDS.txt')