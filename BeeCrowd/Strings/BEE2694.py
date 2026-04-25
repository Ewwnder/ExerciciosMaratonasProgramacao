N = int(input())

for _ in range(N):
    linha = input().strip()

    numero1 = int(linha[2:4])
    numero2= int(linha[5:8])
    numero3 = int(linha[11:13])

    print(numero1+numero2+numero3)


    