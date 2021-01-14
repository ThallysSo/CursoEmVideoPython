soma_impares = 0
for i in range(1, 500, 2): # somando apenas números impares diminuindo o loop
    if i % 3 == 0:
        soma_impares += i
print(soma_impares)
