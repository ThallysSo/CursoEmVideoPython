primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 1
resposta = 1
termo = 11
while True:
    while c < termo:
        print('{}º é {}'.format(c, primeiro_termo + ((c - 1) * razao - primeiro_termo)))
        c += 1
    if resposta != 0:
        resposta = int(input('Digite até quantos termos você quer ver: '))
        termo = resposta + 1
    else:
        break
