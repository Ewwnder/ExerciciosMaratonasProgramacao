J, R = map(int, input().split())

pontos = list(map(int, input().split()))

pontuacao = [0]*J

for i in range(J*R):
    jogador = i%J
    pontuacao[jogador]+=pontos[i]

maior = max(pontuacao)

for i in range(J-1, -1, -1):
    if pontuacao[i]==maior:
        print(i+1)
        break