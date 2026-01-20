N, C = map(int, input().split())

quantidade_elevador = 0
excedeu = False

for _ in range(N):
    S, E = map(int, input().split())

    quantidade_elevador = (quantidade_elevador-S) + E

    if quantidade_elevador>C:
        excedeu = True

if excedeu:
    print("S")
else:
    print("N")

