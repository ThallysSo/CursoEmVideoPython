n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
while True:
    print('[ 1 ] Somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    resposta = int(input('Opção: '))
    if resposta == 1:
        print(n1 + n2)
    elif resposta == 2:
        print(n1 * n2)
    elif resposta == 3:
        if n1 > n2:
            print('A 1º opção é maior. ')
        else:
            print('A 2º opção é maior. ')
    elif resposta == 4:
        n1 = int(input('Digite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))
    elif resposta == 5:
        break
    else:
        print('Opção Inválida')
print('SAINDO...')
