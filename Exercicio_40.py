n1 = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Reprovado!')
elif media >= 5 and media < 7:
    print('Recuperação!')
else:
    print('Aprovado!')
