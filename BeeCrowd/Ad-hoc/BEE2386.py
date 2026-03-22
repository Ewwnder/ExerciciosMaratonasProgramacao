A = int(input())
N = int(input())

contador_percebidas = 0

for _ in range(N):
    estrela = int(input())

    enxergar = A*estrela

    if enxergar>=40000000:
        contador_percebidas+=1

print(contador_percebidas)