entradas = 0
saidas = 0
pessoas = 0

while True:
    entrada = input().split()

    if entrada[0] == "ABEND":
        break

    X = int(entrada[1])

    if entrada[0] == "SALIDA":
        entradas+=1
        pessoas+=X
    elif entrada[0] == "VUELTA":
        saidas+=1
        pessoas-=X

carros = entradas-saidas

print(pessoas)
print(carros)
