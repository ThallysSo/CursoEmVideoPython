s = contador = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    s += n
    contador += 1
print('Somatório: {}'.format(s))
print('Quantidade de números digitados: {}'.format(contador))
