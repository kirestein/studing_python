# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]



""" lista.sort(key=lambda item: item['nome']) # * cria uma cópia raza da minha lista

for item in lista:
    print(item) """


print()
'''
# ! A palavra lambda equivale a palavra def
# Context from functions/lambda.py:exibir
# * o primeiro item que aparece é o parametro passado para a função

'''
l1 = sorted(lista, key=lambda item: item['nome'])
print(f'{l1=}')
print('-' * 100)
l2 = sorted(lista, key=lambda item: item['sobrenome'])
print(f'{l2=}')
print('-' * 100)
lista.sort(key=lambda item: item['nome'])
# lista.sort(key=lambda item: item['sobrenome'])
def exibir(lista):
    for item in lista:
        print(f'{item=}')
    print('-' * 100)
    
exibir(l1)
exibir(l2)