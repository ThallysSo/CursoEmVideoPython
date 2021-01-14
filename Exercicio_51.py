primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for n in range(1, 11):
    print('{}º é {}'.format(n, primeiro_termo + ((n - 1) * razao - primeiro_termo)))
