N1, D1, V1 = map(int, input().split())
N2, D2, V2 = map(int, input().split())

primeira_charrete = D1/V1
segunda_charrete  = D2/V2

if primeira_charrete<segunda_charrete:
    print(N1)
else:
    print(N2)