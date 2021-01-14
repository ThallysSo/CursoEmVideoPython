lista = [0, 1]
primeiroNum = 0
segundoNum = 1
entrada = int(input("Digite o numero: "))
contador = 0

while contador <= entrada - 3:
    proximoNumero = lista[primeiroNum] + lista[segundoNum]
    lista.append(proximoNumero)
    primeiroNum += 1
    segundoNum += 1
    contador += 1
print(lista)
