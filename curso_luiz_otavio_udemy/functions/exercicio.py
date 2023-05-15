'''
Crie funções que duplicam, triplicam e quadriplicam o número recebido como parâmetro
'''
def criar_multiplicador(multiplicador):
    def multiplicar(n):
        return f'{multiplicador} x {n} = {n * multiplicador}'
    return multiplicar
n = int(input('Digite um número: '))
duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)
print(duplicar(n))
print(triplicar(n))
print(quadriplicar(n))
'''
Crie uma função que recebe um número e retorna True se ele é par ou False se ele é ímpar
'''
def par(n):
    if n % 2 == 0:
        return True
    else:
        return False
n = int(input('Digite um número: '))
print(par(n))
'''
Crie uma função que recebe um número e retorna True se ele é primo ou False se ele não é primo
'''
def primo(n):
    if n % 2 == 0 and n > 2 and n != 1:
        return False
    else:
        return True
n = int(input('Digite um número: '))
print(primo(n))
'''
Crie uma função que recebe um número e retorna o seu fatorial
'''
def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat
n = int(input('Digite um número: '))
print(fatorial(n))
'''
Crie uma função que recebe um número e retorna True se ele é um número perfeito ou False se ele não é um número perfeito
''' 
def perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    if soma == n:
        return True
    else:
        return False
n = int(input('Digite um número: '))
print(perfeito(n))