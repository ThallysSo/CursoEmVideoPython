dia = int(input('Digite a quantidade de dias alugados: '))
km = float(input('Digite a quantidade de km percorridos: '))
print('O valor a pagar por {} dias percorridos é de R$ {:.2f} reais.'.format(dia, (60 * dia) + (km*0.15)))
