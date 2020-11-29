def redacting(sentence,redact):
    return sentence.replace(redact,'REDACTED')
t = (input('enter the sentence : '),input('enter the redact : '))
print(f'The redacted sentence is : {redacting(t[0],t[1])}')
