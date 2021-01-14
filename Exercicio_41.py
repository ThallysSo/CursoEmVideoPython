from datetime import datetime

ano_atual = datetime.now().year
ano = int(input('Digite seu ano de nascimento: (YYYY): '))
resultado = ano_atual - ano
if resultado < 9:
    print('Você tem {} anos e é MIRIM!'.format(resultado))
elif resultado < 14:
    print('Você tem {} anos e é INFANTIL!'.format(resultado))
elif resultado < 19:
    print('Você tem {} anos e é JÚNIOR!'.format(resultado))
elif resultado < 20:
    print('Você tem {} anos e é SÊNIOR!'.format(resultado))
else:
    print('Parabéns, velhinho!')
