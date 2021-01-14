valor_sacar = int(input('Digite o valor a ser sacado: R$ '))
cinquenta = vinte = dez = um = 0
while True:
    if valor_sacar >= 50:
        cinquenta += 1
        valor_sacar -= 50
    elif valor_sacar >= 20:
        vinte += 1
        valor_sacar -= 20
    elif valor_sacar >= 10:
        dez += 1
        valor_sacar -= 10
    elif valor_sacar >= 1:
        um += 1
        valor_sacar -= 1
    else:
        break
if cinquenta != 0:
    if cinquenta == 1:
        print(f'{cinquenta} cédula de 50')
    else:
        print(f'{cinquenta} cédulas de 50')
if vinte != 0:
    if vinte == 1:
        print(f'{vinte} cédula de R$20')
    else:
        print(f'{vinte} cédulas de R$20')
if dez != 0:
    if dez == 1:
        print(f'{dez} cédula de R$10')
    else:
        print(f'{dez} cédulas de R$10')
if um != 0:
    if um == 1:
        print(f'{um} cédula de R$1')
    else:
        print(f'{um} cédulas de R$1')
