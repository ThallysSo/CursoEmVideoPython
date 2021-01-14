print('*-=' * 8)
print('Programa de Estatística')
print('*-=' * 8)
maior_18 = homens = mulheres = 0
resposta = 's'
while resposta == 's':
    idade = int(input('Idade: '))
    sexo = input('Sexo [M / F]: ').strip().lower()
    while sexo not in 'mf':
        sexo = input('Sexo [M / F]: ').strip().lower()
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheres += 1
    if idade >= 18:
        maior_18 += 1
    print('-' * 25)
    resposta = input('Quer continuar? [S / N] ').strip().lower()
    print('-' * 25)
    while resposta not in 'sn':
        resposta = input('Quer continuar? [S / N] ').strip().lower()
        print('-' * 25)
print(f'Total de pessoas com mais de 18 anos {maior_18}')
print(f'Ao todo temnos {homens} homens cadastrados')
print(f'Temos {mulheres} mulheres com menos de 20 anos')
