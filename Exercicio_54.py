from datetime import date

maioridade = 0
menoridade = 0
for i in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - ano
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print('{} pessoas já atingiram a maioridade!'.format(maioridade))
print('{} pessoas não atingiram a maioridade!'.format(menoridade))