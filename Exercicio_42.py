a = int(input('Digite o 1º lado: '))
b = int(input('Digite o 2º lado: '))
c = int(input('Digite o 3º lado: '))

if a < b + c and b < a + c and c < a + b:
    print('TRIÂNGULO')
    if a == b and b == c:
        print('E é um triângulo equilátero!')
    elif a == b or b == c or a == c:
        print('E é um triângulo isóceles!')
    elif a != b and a != c:
        print('E é um triângulo escaleno!')
else:
    print('Não vai ter triângulo!')