def copy(str1, str2, index = 0):
    if len(str1) == len(str2):
        return f'copied string : {str2}'
    str2 += str1[index]
    return copy(str1, str2, index = index + 1)
    
str1 = input('enter the string : ')
str2 = ''
print(copy(str1, str2))
