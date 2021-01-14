lista = []
resposta = 's'
while resposta == 's':
    numero = int(input('Digite um valor: '))
    if numero not in lista:
        lista.append(numero)
        print('Adicionado com Sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resposta = input('Quer continuar? [S / N] ').strip().lower()[0]
lista.sort()
print(f'Você digitou os valores {lista}')