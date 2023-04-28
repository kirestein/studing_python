def saudacao(msg):
    return msg

def executa(function, *args):
    return function(*args)

print(executa(saudacao, 'Bom dia'))