
def potential(word):
    return sum([ord(c) for c in word])


with open('resources/Sentence.txt', 'r') as sentence_file:
    content = sentence_file.read()
    for letter in content:
        if letter in ('.', '?', '!'):
            sentence = content.split(letter)[0].strip()
            print(sentence + letter)

            words = sentence.split()
            decoded_sentence = ' '.join(sorted(words, key=potential))
            print(decoded_sentence)
            break
