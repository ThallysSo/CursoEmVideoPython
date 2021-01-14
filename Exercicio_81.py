lista = []
resposta = 's'
while resposta == 's':
    lista.append(int(input('Digite um valor: ')))
    resposta = input('Quer continuar? [S / N] ')
print(f'Números digitados: {len(lista)}')
lista.sort(reverse=True)
print(f'Ordenada de forma descrescente: {lista}')
if 5 in lista:
    print('O 5 está na lista')
else:
    print('O 5 não está na lista')
