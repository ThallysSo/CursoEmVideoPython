print(f'{"LOJAS DO CAMPEÃO":=^30}')
produto = int(input('Digite o valor do produto: R$ '))
print('\033[2;31m [ 1 ]\033[m \033[2;32mÀ vista no dinheiro - 10% de desconto\033[m ')
print('\033[2;31m [ 2 ]\033[m \033[2;32mÀ vista no cartão - 5% de desconto\033[m  ')
print('\033[2;31m [ 3 ]\033[m \033[2;32mEm até 2x no cartão - Preço normal\033[m  ')
print('\033[2;31m [ 4 ]\033[m \033[2;32m3x ou mais no cartão - 20% de juros\033[m  ')
resposta = int(input('Opção: '))
if resposta == 1:
    print('À vista no dinheiro R${:.2f}'.format(produto - (produto * 0.1)))
elif resposta == 2:
    print('À vista no cartão R${:.2f}'.format(produto - (produto * 0.05)))
elif resposta == 3:
    print('Em até 2x no cartão R${:.2f}'.format(produto))
    print('2x de R${:.2f}'.format(produto/2))
elif resposta > 3:
    parcelas = int(input('Quantas parcelas: '))
    com_juros = produto + (produto * 0.2)
    print('{}x de R${:.2f}'.format(parcelas, com_juros/parcelas))
else:
    print('Forma de pagamento inválida! ')
