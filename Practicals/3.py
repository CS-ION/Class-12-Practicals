def cipher(text, shift):
    encrypted_text=''
    for I in text:
        if I>='A' and I<='Z':
            asci = ord(I) + shift
            if asci>90:
                asci = 64 + (asci-90)
            encrypted_text += chr(asci)
        elif I>='a' and I<='z':
            asci = ord(I) + shift
            if asci>122:
                asci= 96 + (asci-122)
            encrypted_text += chr(asci)
        else:
            encrypted_text += I
    return f'encrypted text : {encrypted_text}'

T = input('enter the text to be encrypted : ')
S = int(input('enter the shift : '))
print(cipher(T,S))