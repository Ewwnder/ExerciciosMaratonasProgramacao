areaTotal = 160*70

B = int(input())
T = int(input())

metade = areaTotal/2

areaEsquerda = 35*(B+T)

if areaEsquerda>metade:
    print("1")
elif areaEsquerda<metade:
    print("2")
else:
    print("0")