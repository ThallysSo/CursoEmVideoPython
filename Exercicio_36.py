from time import sleep
cores = {
    'verde': '\033[2;32m',
    'vermelho': '\033[2;31m',
    'azul': '\033[2;34m',
    'limpa': '\033[m'
}
print(12*'{}=_{}'.format(cores['azul'], cores['limpa']))
print('{}PROGRAMA DE EMPRÉSTIMOS{}'.format(cores['azul'], cores['limpa']))
print(12*'{}=_{}'.format(cores['azul'], cores['limpa']))
casa = int(input('Valor da casa: '))
salario = int(input('Salário: '))
anos = int(input('Em quantos anos pretende pagar: '))

meses = anos * 12
prestacao = casa / meses
porcentagem = salario * 0.3

print('{}Analisando...{}'.format(cores['verde'], cores['limpa']))
sleep(1)
print('Quantidade de meses do parcelamento: {}{} meses{}'.format(cores['azul'], meses, cores['limpa']))
print('Valor do financiamento: {}R${}{}'.format(cores['azul'], prestacao, cores['limpa']))
print('30% do seu salário: {}R${}{}'.format(cores['azul'], int(porcentagem), cores['limpa']))

print('{}RESULTADO{}'.format(cores['vermelho'], cores['limpa']))
if prestacao > porcentagem:
    print('{}Infelizmente não será possível conceder o empréstimo.'.format(cores['vermelho']))
elif prestacao < porcentagem:
    print('{}Parabéns, você conseguiu o financiamento!'.format(cores['verde']))
