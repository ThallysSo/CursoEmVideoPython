a = int(input('Digite o 1º lado: '))
b = int(input('Digite o 2º lado: '))
c = int(input('Digite o 3º lado: '))

if a < b + c and b < a + c and c < a + b:
    print('TRIÂNGULO')
else:
    print('Não vai ter triângulo!')