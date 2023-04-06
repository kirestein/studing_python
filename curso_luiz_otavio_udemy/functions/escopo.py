x = 5

def escopo(x): #se eu vou apenas utilizar o valor da variável global, posso apenas referênciá-lo.
    print(f'{x=}')
    x = 2
    print(f'{x=}')
    
escopo(x) # se dentro da função vou fazer alguma tratativa com o valor da variável global, é de boa prática, passar este valor como argumento da função