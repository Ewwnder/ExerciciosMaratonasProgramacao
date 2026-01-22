while True:
    T, N = map(int, input().split())

    if T == 0 and N == 0:
        break

    soma_pontos = 0

    for _ in range(T):
        time, pontos = input().split()
        soma_pontos += int(pontos)

    empates = 3 * N - soma_pontos
    print(empates)