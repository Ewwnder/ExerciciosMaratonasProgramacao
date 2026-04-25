while True:
    A, C = map(int, input().split())

    if A == 0 and C == 0:
        break

    comprimentos = list(map(int, input().split()))

    qnt = A-comprimentos[0]
    anterior = comprimentos[0]

    for x in comprimentos[1:]:
        if x<anterior:
            qnt+=anterior-x
        anterior = x

    print(qnt)