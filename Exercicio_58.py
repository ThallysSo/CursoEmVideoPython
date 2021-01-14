from random import randint
c = 0
numero = randint(1, 10)
while True:
    n = int(input('Adivinhe o número: '))
    c += 1
    if numero == n:
        break
    elif n < numero:
        print('Mais... Tente outra vez!')
    elif n > numero:
        print('Menos... Tente outra vez!')
print('Você acertou! Precisou de {} tentativas'.format(c))
