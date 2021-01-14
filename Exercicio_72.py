por_extenso = (
    'zero',
    'um',
    'dois',
    'três',
    'quatro',
    'cinco',
    'seis',
    'sete',
    'oito',
    'nove',
    'dez',
    'onze',
    'doze',
    'treze',
    'quatorze',
    'quinze',
    'dezesseis',
    'dezessete',
    'dezoito',
    'dezenove',
    'vinte')

resposta = 's'
while resposta == 's':
    while True:
        numero = int(input('Digite um número: '))
        if numero < 0 or numero > 20:
            print('Tente novamente!')
        else:
            break
    for c in range(0, len(por_extenso)):
        if numero == c:
            print(f'O número por extenso é {por_extenso[c]}')
    resposta = input('Quer continuar? [S / N] ').strip().lower()[0]
