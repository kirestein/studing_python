menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    option = input(menu).lower()
    
    if option == 'd':
        pass
    elif option == 's':
        pass
    elif option == 'e':
        pass
    elif option == 'q':
        pass
    else:
        print('Operação inválida, por favor selecione uma operação válida!')