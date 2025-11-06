teste = 1

while True:
    N = int(input())
    if N == 0:
        break

    ingressos = list(map(int, input().split()))

    for i, num in enumerate(ingressos, start=1):
        if i == num:
            ganhador = num
            break

    print(f"Teste {teste}")
    print(ganhador)
    print()
    
    teste+=1
