def saudacao(msg, name):
    return f'{msg}, {name}'

def executa(function, *args):
    return function(*args)



print(executa(saudacao, 'Bom dia', input('Enter your full name: ')))