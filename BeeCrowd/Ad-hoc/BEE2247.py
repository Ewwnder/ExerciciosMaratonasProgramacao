teste = 1

while True:
    N = int(input())
    if N==0:
        break

    diferenca = 0
    print(f"Teste {teste}")

    for _ in range(N):
        J, Z = map(int, input().split())
        diferenca+=(J-Z)
        print(diferenca)

    print()
    teste+=1