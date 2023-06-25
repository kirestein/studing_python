#
# ! Exemplo de uso dos sets
letra_digitada = set()
while True:
    letra = input('Digite uma letra: ')
    letra_digitada.add(letra)
    if letra == 's':
        break
    print(letra_digitada)