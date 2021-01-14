velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('Você foi multado!')
    print('Pague R${} reias por ter ultrapassado {} km acima do limite.'.format((velocidade-80) * 7, velocidade-80))
else:
    print('Digija com cuidado!')