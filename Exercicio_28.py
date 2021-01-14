from random import randint
from time import sleep

numero = int(input('Digite um número entre 0 e 5: '))
r = randint(0, 5)
print('Processando...')
sleep(2)
if r == numero:
    print('Você acertou!')
else:
    print('Você errou! Eu escolhi {}.'.format(r))
