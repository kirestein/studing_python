def executa(funcao, *args):
    return funcao(*args)


# def soma(x, y):
#     return x + y

# * função lambida para soma
soma = lambda x, y: x + y
print(f'O resultado da adição de 2 e 3 é: {soma(2, 3)}')


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))

# duplica = cria_multiplicador(2)




print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)