primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 1
while c < 11:
    print('{}º é {}'.format(c, primeiro_termo + ((c - 1) * razao - primeiro_termo)))
    c += 1
