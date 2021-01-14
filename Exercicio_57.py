while True:
    sexo = input('Digite o sexo: ').upper().strip()
    if sexo == 'M' or sexo == 'F':
        break
    else:
        print('Digite um sexo válido! ')
if sexo == 'M':
    print('Você é do sexo masculino! ')
else:
    print('Você é do sexo feminino! ')