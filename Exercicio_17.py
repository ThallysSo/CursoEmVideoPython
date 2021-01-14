from math import sqrt, hypot

co = float(input('Cumprimento do cateto oposto: '))
ca = float(input('Cumprimento do cateto adjcente: '))
# hipotenusa = sqrt(pow(co, 2) + pow(ca, 2))
hipotenusa = hypot(co, ca)
print('Hipotesuna: {:.2f}'.format(hipotenusa))