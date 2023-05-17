menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def sacar(valor):
    global numero_saques, saldo, extrato
    saldo -= valor
    print('Saque efetuado com sucesso')
    print(f'Seu saldo atual é de: R${saldo:.2f}')
    extrato.append(f'Saque: R${valor:.2f}')
    numero_saques += 1
    print(f'Você ainda possui {numero_saques} saques para realizar.')

def depositar(valor):
    global saldo, extrato
    if valor <=0:
        print('Você não pode depositar valores iguais ou menores que zero.')
        return
    saldo += valor
    print('Depósito efetuado com sucesso')
    extrato.append(f'Depósito: R${valor:.2f}')

def imprimir_extrato():
    if extrato == []:
        print('Você ainda não fez nenhuma operação')
        return
    print('Extrato:')
    for op in extrato:
        print(op)
        print('')
    print(f'Saldo: R${saldo:.2f}')
    print('')
    print(f'Número de saques: {numero_saques}/{LIMITE_SAQUES}')


while True:
    option = input(menu).lower()
    
    if option == 'd':
        valor_depositar = int(input('Qual o valor que vc deseja depositar? R$'))
        depositar(valor_depositar)
    
    elif option == 's':
        valor_sacar = int(input('Qual valor vc deseja sacar? R$'))
        if valor_sacar > saldo:
            print(f'Você não pode sacar este valor, pois seu saldo é apenas de R${saldo:.2f}')
            continue
        if numero_saques == 3:
            print('Você não excedeu o número de saques para o dia de hoje')
            continue
        sacar(valor_sacar)
        
    elif option == 'e':
        imprimir_extrato()
    
    elif option == 'q':
        confirm = input('Você está certo de que deseja sair do sistema? [s/n]').lower()
        if confirm.lower() == 's':
            print('Saindo do sistema...')
            break
        else:
            print('Ok, continuando no sistema...')
            continue
    else:
        print('Operação inválida, por favor selecione uma operação válida!')