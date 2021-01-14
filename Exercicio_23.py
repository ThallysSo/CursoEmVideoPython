# numero = int(input('Digite um número: '))
# print('Unidade:', numero % 10)
# print('Dezena:', numero // 10 % 10)
# print('Centena:', numero // 100 % 10)
# print('Milhar:', numero // 1000)
while True:
    numero = int(input('Digite um número: '))
    numero = ' '.join(str(numero))
    numero = numero.split()
    if len(numero) == 4:
        print('Unidade:{} \nDezena:{} \nCentena:{} \nMilhar:{}'.format(numero[3], numero[2], numero[1], numero[0]))
    elif len(numero) == 3:
        print('Unidade:{} \nDezena:{} \nCentena:{}'.format(numero[2], numero[1], numero[0]))
    elif len(numero) == 2:
        print('Unidade:{} \nDezena:{}'.format(numero[1], numero[0]))
    else:
        print('Unidade:{}'.format(numero[0]))