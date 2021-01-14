lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25.00, 'Transferidor', 4.20, 'Mochila', 120.74, 'Computador', 1250.45)

print('-' * 40)
print('{:^38}'.format('LISTAGEM DE PREÇOS'))
print('-' * 40)

for c in range(0, len(lista) - 1, 2):
    print(lista[c], end='')
    print('.' * (30 - len(lista[c])), end='')
    print(f'R$  {lista[c + 1]:>7.2f}')
