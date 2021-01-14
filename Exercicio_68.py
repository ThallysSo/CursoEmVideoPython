from random import randint
from time import sleep
from os import path


def animacao():
    sleep(0.3)
    print('UM', end='')
    sleep(0.1)
    print(' DÓ', end='')
    sleep(0.1)
    print(' LÁ', end='')
    sleep(0.1)
    print(' SI', end='')
    sleep(0.1)
    print(' E ', end='')
    sleep(0.3)
    print('MEIO ', end='')
    sleep(0.3)
    print('E')
    sleep(0.6)
    print('\033[2;31mJÁ\033[m')


nome = input('Digite seu nome: ')
print('-=' * 10)
print('RECORDE DE VITÓRIAS CONSECUTIVAS')

if path.exists('ranking.txt'):
    with open('ranking.txt', 'r') as r1:
        for linha in r1.readlines()[0::]:
            print(str(linha.split(',')[0]))
else:
    with open('ranking.txt', 'w') as r2:
        r2.writelines(' ')

vitorias_consecutivas = 0
while True:
    print('-=' * 10)
    print('[ 1 ] PAR\n[ 2 ] ÍMPAR ')
    opcao = int(input('').strip().lower())
    n = int(input('Digite o valor: '))
    computador = randint(1, 5)
    print('-=' * 10)
    animacao()
    print(f'Jogador:{n}')
    print(f'Computador:{computador}')
    resultado = n + computador
    print(f'Resultado:{resultado}')
    if resultado % 2 == 0:
        if opcao == 1:
            print('\033[2;32mJogador VENCEU!\033[m')
            vitorias_consecutivas += 1
        elif opcao == 2:
            print('\033[2;31mJogador PERDEU!\033[m')
            break
    elif resultado % 2 != 0:
        if opcao == 2:
            print('\033[2;32mJogador VENCEU!\033[m')
            vitorias_consecutivas += 1
        elif opcao == 1:
            print('\033[2;31mJogador PERDEU!\033[m')
            break
print(f'Total de vitórias consecutivas {vitorias_consecutivas} VITÓRIAS')

with open('ranking.txt', 'r') as ranking:
    for linha in ranking.readlines()[0::]:
        if str(linha) == ' ':
            with open('ranking.txt', 'w') as r3:
                r3.writelines(f'{nome}: {vitorias_consecutivas}')
        elif int(linha.split(':')[1]) < vitorias_consecutivas:
            with open('ranking.txt', 'w') as r:
                r.writelines(f'{nome}: {vitorias_consecutivas}')
