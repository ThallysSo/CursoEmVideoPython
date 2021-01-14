from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

for c in numeros:
    print('[', c, ']')
print('MAIOR: ', end='')
print(max(numeros))
print('MENOR: ', end='')
print(min(numeros))
