peso = float(input('Digite seu peso em (Kg): '))
altura = float(input('Digite sua altura em (m): '))
imc = peso / (pow(altura, 2))
print('IMC: {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso ideal. ')
elif imc < 30:
    print('Sobrepeso.')
elif imc < 40:
    print('Obesidade.')
else:
    print('Obesidade Mórbida.')
