numero = int(input('Digite um número: '))
print('Par ou Impar')
if numero % 2 == 0:
    print('PAR!')
else:
    print('IMPAR!')

print('Números Primos')
primo = 0
for i in range(1, numero+1):
    if numero % i == 0:
        primo += 1
if primo <= 2:
    print('PRIMO!')
else:
    print('Não é dos nossos.')