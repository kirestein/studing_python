import random
# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiply(*args):
    total = 1
    try:
        for arg in args:
            total *= arg
        print(f'{total=}')
    except:
        print('You passed a argument was not a number: ')

multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)




# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def even_odd(*args):
    try:
        for arg in args:
            if arg % 2 == 0:
                print(f'{arg} is even')
            else:
                print(f'{arg} is odd')
                
    except:
        print('You passed a argument was not a number: ')
        

list_of_numbers = []

for i in range(10):
    number = random.randint(0, 1000)
    list_of_numbers.append(number)

even_odd(1,5,46,84,46,99,10,56,32,15,64,67,19)