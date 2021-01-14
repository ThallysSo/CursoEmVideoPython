from math import cos, sin, tan, radians
# Transformação necessária para radianos
n = float(input('Digite o tamanho do ângulo: '))
print('Cosseno: {:.1f} \nSeno: {:.1f} \nTangente: {:.1f}'.format(cos(radians(n)), sin(radians(n)), tan(radians(n))))