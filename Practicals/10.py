def multiplication(N , multiplier = 1):
    if multiplier == 11:
        return
    print(f'{N}*{multiplier}={N*multiplier}')
    multiplication(N,multiplier = multiplier + 1)
n = int(input('enter the number : '))
multiplication(n)