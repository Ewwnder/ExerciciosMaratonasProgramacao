N = int(input())

for _ in range(N):
    M = int(input())

    notas = list(map(int, input().split()))

    ordem_fila = sorted(notas, reverse=True)
    contador = 0

    for i in range(M):
        if notas[i]==ordem_fila[i]:
            contador+=1
    
    print(contador)