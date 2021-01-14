lista = []

expressao = input('Digite a expressão: ').strip()
lista.append(expressao)
parentese_1 = parentese_2 = 0

for c in expressao:
    if c in '(':
        parentese_1 += 1
    if c in ')':
        parentese_2 += 1
if parentese_1 == parentese_2:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
