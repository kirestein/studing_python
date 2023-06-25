""" 
    # ! List Comprehension em Python
    List Comprehension é uma forma rápida para criar listas.
    Com list comprehension, você cria uma lista a partir de uma expressão composta.
    A partir de iteráveis, você cria uma nova lista.
"""
from pprint import pprint as pp

# print(list(range(10))) # ! vamos partir daqui para gerar nossa list comprehension

lista = []
for i in range(10):
    lista.append(i)
print('modo tradicional:', lista)

lista = [i * 2 if i % 2 == 0 else i for i in range(10)]
print('com list comprehension:', lista)
print('-' * 50)

# ? Mapeamento de dados com List Comprehension
produtos = [
    {
        'nome': 'Notebook',
        'preco': 2000,
    },
    {
        'nome': 'Impressora',
        'preco': 800,
    },
    {
        'nome': 'Cadeira',
        'preco': 80
    },
    {
        'nome': 'Copo',
        'preco': 5
    }
]

dados = [(produto['nome'], produto['preco']) for produto in produtos]
print(*dados, sep='\n') # ! este asterisco serve para desempacotar a lista
print('-' * 50)

dados_02 = [{**produto} for produto in produtos] # * Estes dois asteriscos servem para desempacotar o dicionário
print(*dados_02, sep='\n') # ! este asterisco serve para desempacotar a lista
print('-' * 50)

print('Filtro')
dados_03 = [{**produto, 'preco': produto['preco'] * 1.2} for produto in produtos if produto['preco'] > 500] # ! se o if for à direita, quer dizer que a condição será aplicada ao for
print(*dados_03, sep='\n') # ! este asterisco serve para desempacotar a lista
print('-' * 50)

print('Mapeamento')
dados_03 = [{**produto, 'preco': produto['preco'] * 1.2} if produto['preco'] < 500 else produto for produto in produtos] # ! se o if for à esquerda, quer dizer que a condição será aplicada antes do for
print(*dados_03, sep='\n')
print('-' * 50)


pp(dados_03, sort_dicts=False) # ? pprint é um móduto do python que cria uma tabela