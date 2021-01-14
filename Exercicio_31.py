distancia = int(input('Digite a quantidade de km que foi gasto: '))
print('Custo de viagem normal: R${} reias'.format(int(distancia*0.5))if distancia <= 200 else 'Custo da viagem com desconto: R${} reais'.format(int(distancia*0.45)))


# if distancia <= 200:
#     print('Custo de viagem normal: R${} reias'.format(int(distancia*0.5)))
# else:
#     print('Custo da viagem com desconto: R${} reais'.format(int(distancia*0.45)))