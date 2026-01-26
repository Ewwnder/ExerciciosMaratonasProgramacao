N = int(input())

alunos_presenca = set()

for _ in range(N):
    V = int(input())

    alunos_presenca.add(V)

print(len(alunos_presenca))