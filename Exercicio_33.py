n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
if n1 > n2 and n1 > n3:
    print('O 1º número é o maior.')
elif n1 < n2 and n1 < n3:
    print('O 1º número é o menor.')
if n2 > n1 and n2 > n3:
    print('O 2º número é o maior.')
elif n2 < n1 and n2 < n3:
    print('O 2º número é o menor.')
if n3 > n2 and n3 > n1:
    print('O 3º número é o maior.')
elif n3 < n2 and n3 < n1:
    print('O 3º número é o menor.')