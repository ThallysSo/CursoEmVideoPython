soma_pares = 0
for i in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma_pares += n
print(soma_pares)
