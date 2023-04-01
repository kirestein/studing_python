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
import re

cpf_recebido = input('Por favor, digite o seu cpf, sem os dois últimos digitos (xxx.xxx.xxx): ')

def tratar_cpf(cpf):
    cpf_tratado = re.sub(
        r'[^0-9]',
        '',
        cpf
    )
    return cpf_tratado

def loop_cpf(cpf, count):
    total = 0
    for i in cpf:
        valor = int(i)
        total += (valor * count)
        count = count - 1
    return total

def calcula_segundo_digito(cpf):
    if len(cpf) > 10:
        cpf_tratado = tratar_cpf(cpf)
    else:
        cpf_tratado = cpf
    total = loop_cpf(cpf_tratado, 11)
    total *= 10
    resto = total % 11
    digito = resto if resto <= 9 else 0
    new_cpf = cpf + str(digito)
    print(f'{new_cpf=}')
    return new_cpf

def calcula_primeiro_digito(cpf):
    if len(cpf) > 9:
        cpf_tratado = tratar_cpf(cpf)
    else:
        cpf_tratado = cpf
    total = loop_cpf(cpf_tratado, 10)
    total *= 10
    resto = total % 11
    digito = resto if resto <= 9 else 0
    new_cpf = cpf + str(digito)
    print(f'{new_cpf=}')
    new_cpf = cpf + '-' + str(digito)
    calcula_segundo_digito(new_cpf)
    return new_cpf
calcula_primeiro_digito(cpf_recebido)



