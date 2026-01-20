N = int(input())

valores = list(map(int, input().split()))

max_sequencia = 1
sequencia_atual = 1

for i in range(1, N):
    if valores[i] == valores[i-1]: #Para não sair do tamanho do vetor irei comparar o atual com o anterior.
        sequencia_atual+=1
    else:
        sequencia_atual = 1
        
    max_sequencia = max(max_sequencia, sequencia_atual)

print(max_sequencia)