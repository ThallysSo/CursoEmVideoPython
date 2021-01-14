for n in range(1, 100):
    numero = int(input('Digite um número: '))
    primo = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            primo += 1
    if primo == 2:
        print('É primo!')
    else:
        print('Não é dos nossos.')
