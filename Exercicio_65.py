c = 0
n = []
while True:
    n.append(int(input('Digite um número: ')))
    c += 1
    resposta = input('Quer continuar? [S / N] ').upper()
    if resposta == 'S':
        continue
    elif resposta == 'N':
        break
    while resposta != 'NS':
        print('Valor Inválido!')
        resposta = input('Quer continuar? [S / N] ').upper()
print(f'Média: {sum(n)/c}')
print(f'Maior valor: {max(n)}')
print(f'Menor valor: {min(n)}')
