def piglatin(string):
        return string[-3] + string[:-3] if string[-2:] == 'ay' else string

word = input()
print(piglatin(word))
