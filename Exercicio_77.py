palavras = ('aprender', 'programar', 'linguagem', 'python')

for p in palavras:
    print(p.upper(), '', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, '', end='')
    print('')
