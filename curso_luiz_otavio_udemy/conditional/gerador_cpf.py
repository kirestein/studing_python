"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
cpf ="746.824.890"
def calcula_segundo_digito(cpf):
    total = 0
    count = 11
    for i in cpf:
        if i == '.' or i == '-':
            continue
        valor = int(i)
        total += (valor * count)
        count = count - 1
    total *= 10
    resto = total % 11
    digito = resto if resto <= 9 else 0
    new_cpf = cpf + str(digito)
    print(f'{new_cpf=}')
    return new_cpf

def calcula_primeiro_digito(cpf):
    total1 = 0
    count = 10
    for i in cpf:
        if i == '.':
            continue
        valor = int(i)
        total1 += (valor * count)
        count = count - 1
    total1 = total1 * 10
    resto = total1 % 11
    digito = resto if resto <= 9 else 0
    new_cpf = cpf + '-' + str(digito)
    print(f'{new_cpf=}')
    calcula_segundo_digito(new_cpf)
calcula_primeiro_digito(cpf)



