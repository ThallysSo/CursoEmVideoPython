while True:
    n = int(input('Quer ver a tabuada de que valor? '))
    if n > 0:
        for c in range(1, 11):
            print(f'{n} x {c} = {n * c}')
    else:
        print('Finalizando Programa...')
        break
