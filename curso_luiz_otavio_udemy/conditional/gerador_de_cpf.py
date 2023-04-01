from validador_cpf import calcula_primeiro_digito
import random as rd

def main():
    cpf = ''
    while len(cpf) < 11:
        for i in range(0, 3):
            num = rd.randint(0, 10)
            cpf += str(num)
        if len(cpf) < 11:
            cpf += '.'
        if len(cpf) > 11:
            cpf = ''
            continue
    calcula_primeiro_digito(cpf)
main()