import os
os.chdir(r'./../../')
os.chdir(r'../Desktop') #changing dir to desktop
os.mkdir('myDir')

file = open('myFile.txt','a+')
lines = '''Here is an example of a text file
This file was created with python
We can write on this file
'''
file.write(lines)
file.close()

os.chdir(r'./mydir')
file = open('temp.txt','a+')
file.write(lines)
file.close()

os.remove('../myFile.txt')
os.rename('temp.txt','myFile.txt')


