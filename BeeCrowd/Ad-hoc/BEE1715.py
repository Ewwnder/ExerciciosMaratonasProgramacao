N, M = map(int, input().split())

jogador = 0

for _ in range(N):
    gols = map(int, input().split())

    if all (g>0 for g in gols):
        jogador+=1

print(jogador)