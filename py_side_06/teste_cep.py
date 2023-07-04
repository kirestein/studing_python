import consulta_correios
import aspose.words as aw
# import pycep_correios
import requests

address = consulta_correios.busca_cep('Rua Raul Jośe Braconaro')
print(address)



cep = "20.090-002"

cep = cep.replace("-", "").replace(".", "").replace(" ", "")
print(cep)

if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link)

    print(requisicao)

    address = requisicao.json()

    uf = address['uf']
    cidade = address['localidade']
    bairro = address['bairro']
    # print(address)
    print(f"Logradouro: {address['logradouro']}")
    print(f"Bairro: {address['bairro']}")
    print(f"Cidade: {address['localidade']}")
else:
    print("CEP Inválido")