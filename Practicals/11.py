from random import choice
sections = ['A','B','C']
class_9 = open('class9.txt','r')
lines_9 = class_9.readlines()
limit = int(len(lines_9)/3) + 1
for I in range(3):
    f = open(f'class10{sections[I]}.txt','w')
    for I in range(limit):
        try:
            line = choice(lines_9)
            f.write(line)
            lines_9.remove(line)
        except:
            pass
    f.close()

