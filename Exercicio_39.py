from datetime import datetime

ano_atual = datetime.now().year
print('Estamos no ano de {}'.format(ano_atual))
ano = int(input('Digite o ano de nascimento YYYY: '))
resultado = ano_atual - ano
if resultado == 16:
    print('Está na hora de se alistar! ')
elif resultado < 16:
    print('Ainda não é seu momento, Campeão!')
    print('Faltam {} anos ainda. '.format(16 - resultado))
else:
    print('Você está atrasado {} anos para o alistamento.'.format(resultado - 16))
