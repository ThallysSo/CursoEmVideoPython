from random import sample

nome1 = input('Digite o nome do primeiro aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('Digite o nome do quarto aluno: ')

lista = [nome4, nome3, nome1, nome2]
print(sample(lista, len(lista)))
