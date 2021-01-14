lista = []

for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        for i in range(0, len(lista)):
            if numero <= lista[i]:
                lista.insert(i, numero)
                break
print(f'Lista: {lista}')
