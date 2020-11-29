def pig_latin(word):
    size = len(word)
    if word[size-2:size:1] != 'ay':
        return word
    return word[size-3] + word[:size-3:]
x = input('enter the word : ')
print(f'the word is {pig_latin(x)}')