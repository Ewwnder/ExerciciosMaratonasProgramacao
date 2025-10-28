A, G, RendA, RendG = map(float, input().split())

calcAlcool = A/RendA
calcGasolina = G/RendG

if calcAlcool<calcGasolina:
    print("A")
else:
    print("G")