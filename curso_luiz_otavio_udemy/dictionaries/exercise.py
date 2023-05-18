
# !Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
erros = 0
for pergunta in perguntas:
    print(f"{pergunta['Pergunta']}")
    print('')
    opcao_selecionada = 0
    for num, opcao in enumerate(pergunta['Opções']):
        print(f'{num}) {opcao}')
        if num == len(pergunta['Opções']) - 1:
            resposta = input('Selecione uma opção: ')
            while True:
                if resposta.isdigit():
                    opcao_selecionada = int(resposta)
                    break
                else:
                    resposta = input('Selecione um opção válida: ')
    print('')
    for num, opcao in enumerate(pergunta['Opções']):
        if opcao_selecionada == num:
            opcao_selecionada = opcao
    print(opcao_selecionada)
    # resposta = input('Digite a resposta: ')
    if opcao_selecionada == pergunta['Resposta']:
        print('Você acertou! ✅')
        acertos += 1
    else:
        print('Você errou! ❌')
        erros += 1
    print('-' * 50)
print(f'Você acertou {acertos} questões!')
print(f'Você errou {erros} questões!')