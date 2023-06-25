# 
# ? Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
l1 = [1, 2, 3, 3, 3, 3, 1, 4]
s1 = set(l1)
l2 = list(s1)
# s1 = {1, 2, 3, 3, 3, 3, 3, 1, 4}
# print(l2)

# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add(1)
s1.add(2) #? add adiciona um elemento
s1.update((1, 2, 3, 'Olá mundo!')) #? update atualiza o set
# print(s1)
s1.discard('Olá mundo!') #? discard remove um elemento pelo valor
# print(s1)
s1.clear() #? clear limpa o set
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1 | s2 #? s3 = {1, 2, 3, 4, 5} ele une os dois sets eliminando os repetidos
print('União: ', s3)
s3 = s1 & s2 #? s3 = {3} ele retorna os elementos presentes em ambos
print('Intersecção: ', s3)
s3 = s1 - s2 #? s3 = {1, 2} ele retorna os elementos que estão em s1 mas não em s2
print('Diferença (s1 - s2): ', s3)
s3 = s2 - s1 #? s3 = {4, 5} ele retorna os elementos que estão em s2 mas não em s1
print('Diferença (s2 - s1): ', s3)
s3 = s1 ^ s2 #? s3 = {1, 2, 4, 5} ele retorna os elementos que não estão em ambos
print('Diferença simétrica: ', s3)
print('-' * 50)