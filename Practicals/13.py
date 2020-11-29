f = open('Sentence.txt','r')
for I in f.readlines():
    size = len(I)
    if I[size-2] in ['.','?','!']:
        pot_sen = []
        pot_val = []
        print(f'Sentence : {I[0:size-1:1]}')
        for J in I[0:size-2:1].split(' '):
            ascival = 0
            for K in J:
                ascival += ord(K)
            print(f'{J} = {ascival}')
            pot_sen.append(f'{J} {ascival}')
            pot_val.append(ascival)
        new_sen = ''
        for M in sorted(pot_val):
            for N in pot_sen:
                if str(M) in N:
                    new_sen += N.split(' ')[0]
                    break
            new_sen += ' '
        print(f'Highest Potential Sentence : {new_sen}\n')
    else:
        print(f"Invalid Sentence : {I}")
