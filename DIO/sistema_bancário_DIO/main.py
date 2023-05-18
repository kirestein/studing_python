def login(cpf, password):
    if cpf == 'admin' and password == 'admin':
        return 'gerente'
    for conta in contas:
        if cpf == conta['CPF'] and password == conta['password']:
            return conta
        else:
            print('CPF ou senha incorretos!')
            return
        
menu_gerente = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Cadastrar cliente
[c] Cadastrar conta corrente
[lc] Listar clientes
[lcc] Listar contas correntes
[q] Sair

=> """

menu_cliente = """

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
clientes = []
contas = []
agencia = '0001'
numero_conta = 0


def sacar(valor, numero_saques, limite_saques, saldo, extrato, limite):
    if numero_saques >= limite_saques:
        print('Você não excedeu o número de saques para o dia de hoje')
        return
    if valor > limite:
        print(f'Você não pode sacar este valor, pois seu limite é de R${limite:.2f}')
        return
    saldo -= valor
    print('Saque efetuado com sucesso')
    print(f'Seu saldo atual é de: R${saldo:.2f}')
    extrato.append(f'Saque: R${valor:.2f}')
    numero_saques += 1
    print(f'Você ainda possui {numero_saques} saques para realizar.')
    print('-' * 100)

def depositar(valor, saldo, extrato):
    if valor <=0:
        print('Você não pode depositar valores iguais ou menores que zero.')
        return
    saldo += valor
    print('Depósito efetuado com sucesso')
    extrato.append(f'Depósito: R${valor:.2f}')
    print('-' * 100)

def imprimir_extrato(saldo, extrato):
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
    print('-' * 100)
    
def criar_cliente(clientes, contas):
    # nome, data de nascimento, cpf e endereço
    CPF = input('Digite o cpf do cliente(xxxxxxxxxxx): ')
    for cliente in clientes:
        if cliente['CPF'] == CPF:
            print('Já existe um cliente com este CPF')
            return
    nome = input('Digite o nome do cliente: ')
    data_nascimento = input('Digite a data de nascimento do cliente(dd/mm/aaaa): ')
    endereço = input('Digite o endereço do cliente(Logradouro, nro - bairro - cidade/sigla estado): ')
    clientes.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'CPF': CPF,
        'endereço': endereço,
        'conta[s]': contas
    })
    print(clientes)
    print(type(clientes))
    print('-' * 100)
   
    # endereço: "logradour, nro - bairro - cidade/estado"
    # somente um cliente por cpf

print(type(clientes))
def criar_conta_corrente(agencia, numero_conta, clientes, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    '''
    agência, número da conta e usuário
    o número da conta é sequencial
    é obrigatório ter um usuário e apenas um usuário por conta
    um usuário pode ter mais de uma conta
    '''
    CPF = input('Digite o cpf do cliente(xxxxxxxxxxx): ')
    for cliente in clientes:
        # print(cliente['CPF'])
        for key, item in cliente.items():
            if CPF == item:
                # print(cliente)
                deseja_depositar = input('Deseja depositar um valor inicial? [s/n]').lower()
                valor_depositar = 0
                if deseja_depositar == 's':
                    valor_depositar = float(input('Qual o valor que vc deseja depositar? R$'))
                saldo_inicial = depositar(valor_depositar, saldo, extrato)
                saldo = saldo_inicial if saldo_inicial != None else 0
                password: input('Digite a sua senha: ')
                while True:
                    if len(password) < 12:
                        print('A senha deve ter no mínimo 12 caracteres')
                        password: input('Digite a sua senha: ')
                    else:
                        break
                cliente['conta[s]'].append({
                    'nome': cliente['nome'],
                    'CPF': cliente['CPF'],
                    'password': password,
                    'agência': agencia,
                    'número da conta': numero_conta + 1,
                    'saldo': saldo,
                    'extrato': extrato,
                    'limite': limite,
                    'número de saques': numero_saques,
                    'limite de saques': LIMITE_SAQUES
                })
                print(f"Conta para o cliente {cliente['nome']} cadastrada com sucesso! ")
                print(cliente)
                return cliente
        else:
            print('Não existe um cliente com este CPF')
            return
    print(clientes)
    print('-' * 100)

def listar_contas(contas):
    print(f'O banco possui atualmente {len(contas)} ativas!')
    for conta in contas:
        print(conta)
    print('-' * 100)

def listar_clientes(clientes):
    print(f'O banco possui atualmente {len(clientes)} clientes!')
    for cliente in clientes:
        print(cliente)
        print(type(cliente))
    print('-' * 100)


while True:
    cpf = input('Digite o seu CPF: ')
    password = input('Digite a sua senha: ')
    user = login(cpf, password)
    if user == 'gerente':
        menu = menu_gerente
        print('Bem vindo(a) gerente!')
        print('-' * 100)
    elif user != None:
        menu = menu_cliente
        print(f'Bem vindo(a) {user["nome"]}!')
        print('-' * 100)
    
    if option == 'd':
        valor_depositar = int(input('Qual o valor que vc deseja depositar? R$'))
        depositar(valor_depositar, saldo, extrato)
    
    elif option == 's':
        valor_sacar = int(input('Qual valor vc deseja sacar? R$'))
        if valor_sacar > saldo:
            print(f'Você não pode sacar este valor, pois seu saldo é apenas de R${saldo:.2f}')
            continue
        
        sacar(valor=valor_sacar, saldo=saldo, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES, extrato=extrato, limit=limite)
        
    elif option == 'e':
        imprimir_extrato(saldo, extrato=extrato)
        
    elif option == 'u':
        criar_cliente(clientes, contas)
        
    elif option == 'c':
        criar_conta_corrente(agencia=agencia, numero_conta=numero_conta, clientes=clientes, saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
        
    elif option == 'lc':
        listar_clientes(clientes)
        
    elif option == 'lcc':
        listar_contas(contas)
    
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