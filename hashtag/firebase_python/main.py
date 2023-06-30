import requests
import json
# Criar o projeto no Firebase
URL = 'https://hashtagvendas-ede6e-default-rtdb.firebaseio.com/'

# Criar o Database (atenção às regras de segurança)
# estrutura de árvore

# Interação com o DB (REST API)
cliente = {
    'cliente': 'Marcelo',
    'email': 'marcelo@pedro.com',
    'Idade': 30,
    'Cidade': 'Rio de Janeiro',
    'Saldo': 10000

}

produto = {
    'codigo': '1.2.3.4,5,1,2.3.4,7.9',
    'preco': '25,27,29',
    'nome': 'Notebook'
}
# Criar uma vanda (POST)
""" request = requests.post(f'{URL}/Vendas/.json', json.dumps(cliente))
print(request)
print(request.text) """

#Criar um novo produto (POST)
""" request_produto = requests.post(f'{URL}/Produto/.json', json.dumps(produto))
print(request_produto)
print(request_produto.text) """

# Editar a venda (PATCH)
produto_alterado = {
    'codigo': '1.2.3.4',
    'preco': 27.50,
    'nome': 'Notebook',
    'quantidade': 25
}
patch_produtos = requests.patch(f'{URL}/Produto/-NYkJQq9WOH2jKglCfI7/.json', json.dumps(produto_alterado))
print(patch_produtos)
print(patch_produtos.text)
print('-'*60)
# Pegar uma venda específica ou todas as vendas (GET)
get_vendas = requests.get(f'{URL}/Vendas/.json')
print(get_vendas)
response = (get_vendas.json())
# list_response = [{**res} for res in response]

print(response)

# Excluir uma venda (DELETE)

# O que seria legal após isso??
# Autenticação