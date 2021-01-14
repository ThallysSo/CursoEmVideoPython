grupo_pessoas = {}
lista = [1, 2, 3, 4]
for i in range(0, 4):
    grupo_pessoas[lista[i]] = [input('Nome: '), int(input('Idade: ')), input('Sexo: [M / F] ').upper()]

media = 0
nome_mais_velho = ''
mais_velho = 0
menos_de_vinte = 0

for pessoa in grupo_pessoas.values():
    media += pessoa[1]
    if pessoa[1] > mais_velho:
        mais_velho = pessoa[1]
        nome_mais_velho = pessoa[0]
    if pessoa[2] == 'F' and pessoa[1] < 20:
        menos_de_vinte += 1


print('Média de idade: {:.0f} anos'.format(media/len(grupo_pessoas)))
print('Mais velho: {}'.format(nome_mais_velho))
print('Mulheres com menos de 20 anos: {}'.format(menos_de_vinte))