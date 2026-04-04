C = int(input())

for _ in range(C):
    B, E = map(int, input().split())

    indo = ''.join(str(i) for i in range(B, E+1))
    voltando = indo[::-1]

    resultado = indo+voltando

    print(resultado)
