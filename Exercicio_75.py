valor = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))
tres = par = 0
for c in range(0, len(valor)):
    if valor[c] == 3 and tres == 0:
        tres = c
    if valor[c] % 2 == 0:
        par += 1

print(f'Noves: {valor.count(9)}')
if tres == 0:
    print('O valor 3 não foi digitado')
else:
    print(f'Posição onde o primeiro 3 apareceu: {tres}')
print(f'Quantos pares: {par}')
