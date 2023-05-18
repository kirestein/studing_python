
T = int(input())

for i in range(T):    
    value = input().split(' ')
    print(value)
    N = int(value[0])
    K = int(value[-1])
    saida = round(N/K) + N%K
    print(saida)