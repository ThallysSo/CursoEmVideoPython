for i in range(1, 100):
    frase = input('Digite uma frase: ').strip().lower()
    frase = frase.split()
    frase = ''.join(frase)
    if frase[::-1] == frase:
        print('É palíndromo.')
    else:
        print('Não é palíndromo.')