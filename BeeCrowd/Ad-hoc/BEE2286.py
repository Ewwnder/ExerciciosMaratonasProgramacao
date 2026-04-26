i = 1

while True:
    N = int(input())

    if N==0:
        break

    nome1 = input().strip()
    nome2 = input().strip()

    print(f'Teste {i}')

    for _ in range(N):
        A, B = map(int, input().split())

        res = nome1 if (A+B)%2==0 else nome2
        print(res)

    print()
    i+=1