print('{:-^40}'.format('ATACADÃO DO SICUEBE'))
resposta = 's'
produtos = []
preco = []
acima_100 = 0
while resposta == 's':
    produtos.append(input('Nome do Produto: '))
    preco.append(int(input('Preço: R$ ')))
    resposta = input('Quer continuar? [S/N] ').strip().lower()
    while resposta not in 'sn':
        resposta = input('Quer continuar? [S/N] ').strip().lower()

print(f'Total gasto: R${sum(preco)}')

mais_caro = 0
for c in range(0, len(preco)):
    if preco[c] > 1000:
        mais_caro += 1
print(f'Temos {mais_caro} produtos que custam mais de R$ 1.000')

nome_mais_barato = ''
for c in range(0, len(preco)):
    if preco[c] == min(preco):
        nome_mais_barato = produtos[c]
print(f'O produto mais barato foi {nome_mais_barato} que custou R${min(preco)}')
