from random import randint
from time import sleep

while True:
    itens = ['Pedra', 'Papel', 'Tesoura']
    print('''[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA''')
    jogador = str(input('Qual a sua jogada? ').strip())
    if jogador != '':
        jogador = int(jogador)
        if jogador >= 0 and jogador <= 2:
            print('PEDRA')
            sleep(0.3)
            print('PAPEL')
            sleep(0.4)
            print('E TESOOOUURA!')
            sleep(0.3)
            computador = randint(0, 2)
            print('-=' * 14)
            print('O computador jogou {}'.format(itens[computador]))
            print('O jogador jogou {}'.format(itens[jogador]))
            print('-=' * 14)
            if computador == 0:  # PEDRA
                if jogador == 0:
                    print('EMPATOU!')
                elif jogador == 1:
                    print('\033[2;32mO Jogador ganhou!\033[m')
                elif jogador == 2:
                    print('\033[2;31mO computador venceu!\033[m')
            elif computador == 1:  # PAPEL
                if jogador == 0:
                    print('\033[2;31mO computador venceu!\033[m')
                elif jogador == 1:
                    print('EMPATOU!')
                elif jogador == 2:
                    print('\033[2;32mO Jogador ganhou!\033[m')
            elif computador == 2:  # TESOURA
                if jogador == 0:
                    print('\033[2;32mO Jogador ganhou!\033[m')
                elif jogador == 1:
                    print('\033[2;31mO computador venceu!\033[m')
                elif jogador == 2:
                    print('EMPATOU!')
        else:
            print('Jogada inválida!')
    else:
        print('Jogada inválida!')