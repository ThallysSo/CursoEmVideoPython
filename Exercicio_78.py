lista = []
maior = []
menor = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('+-' * 30)
print(f'Você digitou os valores {lista}')
maximo = max(lista)
minimo = min(lista)
for valor in range(0, len(lista)):
    if maximo == lista[valor]:
        maior.append(f'{valor}...')
    elif minimo == lista[valor]:
        menor.append(f'{valor}...')
print(f'Maior: {maximo}, Posição:', *maior)
print(f'Menor: {minimo}, Posição:', *menor)
