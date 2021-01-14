lista = []
resposta = 's'
while resposta == 's':
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    resposta = input('Quer continuar? [S / N] ')

par = []
for c in lista:
    if c % 2 == 0:
        par.append(c)

impar = []
for c in lista:
    if c % 2 == 1:
        impar.append(c)

print(f'Lista completa: {lista}')
print(f'Pares: {par}')
print(f'Impares: {impar}')