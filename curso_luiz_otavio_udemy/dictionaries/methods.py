from copy import deepcopy #? Este módulo permite copiar completamente um dicionário
#! Métodos úteis dos dicionários em Python

pessoa = {
    'nome': 'Prof(a). Ana',
    'idade': 38,
    'cursos': ['Inglês', 'Português']
}


# len - quantas chaves !não é um método
print('len')
print('')
print(len(pessoa))
print('-' * 50)
# keys - iterável com as chaves
print('keys')
print('')
print(pessoa.keys())
print('')
chave = list(pessoa.keys())
print(chave)
print('')
for key in pessoa:
    print(key)
# values = iterável com os valores
print('-' * 50)
print('values')
print('')
for value in pessoa.values():
    print(value)
# items - iterável com chaves e valores
print('-' * 50)
print('items')
print('')
for key, item in pessoa.items():
    print(f'{key}: {item}')
# setdefault - adiciona valor se a chave não existe
print('-' * 50)
print('setdefault')
print('')
pessoa.setdefault('email', None)
print(pessoa)
print('-' * 50)
# update - atualiza o dicionário com outro dicionário ou com um iterável de pares
print('update')
print('')
'''
no update podemos utilizar objetos iteráveis
'''
pessoa.update({
    'nome': 'João',
    'idade': 27,
    'sexo': 'M'
})
print(pessoa)
print('-' * 50)
# clear - limpa o dicionário
# copy - retorna uma cópia rasa (shallow copy)
print('Shallow Copy')
print('')
nova_pessoa = pessoa.copy() 
#* Aqui estou gerando um cópia do dicionário
#* importante frizar que a shallow copy, não copia dados mutáveis, 
#* quando tem dados mutáveis ele faz com que ambos os dicionários
#* apontem para o mesmo dado
print(nova_pessoa)
print('-' * 50)
print('Deep copy')
print('')
nova_pessoa = deepcopy(pessoa) #? neste método ele copia tudo, inclusive os dados mutáveis
print(nova_pessoa)
print('-' * 50)
# get - obtém uma chave
print('get')
print('')
nome = pessoa.get('nome')
print(nome)
print('-' * 50)
# pop - remove uma chave e retorna o valor
print('pop')
print('')
sem_nome = nova_pessoa.pop('nome')
print(sem_nome)
print('')
print(nova_pessoa)
print('-' * 50)
# popitem - remove uma chave-valor e retorna o par
print('popitem')
print('')
ultima_chave = nova_pessoa.popitem()
print(ultima_chave)
print('')
print(nova_pessoa)
print('-' * 50)

