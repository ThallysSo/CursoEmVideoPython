salario = float(input('Digite o salário: '))
if salario > 1250:
    print('Seu novo salário: R${}'.format(salario + (salario * 0.1)))
else:
    print('Seu novo salário: R${}'.format(salario + (salario * 0.15)))
