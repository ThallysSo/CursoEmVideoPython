cores = {
    'verde': '\033[2;32m',
    'vermelho': '\033[2;31m',
    'azul': '\033[2;34m',
    'limpa': '\033[m'
}

print(10 * '{}=_{}'.format(cores['azul'], cores['limpa']))
print('BASE DE CONVERSÃO')
print(10 * '{}=_{}'.format(cores['azul'], cores['limpa']))
resp = 'S'
while resp == 'S':
    n = int(input('Digite um número: '))

    print('Agora, escolha para qual base irá converter!')

    print('{}<1> Binário'.format(cores['azul']))
    print('<2> Hexadecimal')
    print('<3> Octal{}'.format(cores['limpa']))
    resposta = int(input('').strip())

    if resposta == 1:
        binario = str(bin(n))
        print('Binário: {}'.format(binario[2:]))
    elif resposta == 2:
        hexadecimal = str(hex(n))
        print('Hexadecimal: {}'.format(hexadecimal[2:]).upper())
    elif resposta == 3:
        octal = str(oct(n))
        print('Octal: {}'.format(octal[2:]))
    else:
        print('Opção inválida!')
    resp = input('Quer continuar? [ S / N]').upper()
