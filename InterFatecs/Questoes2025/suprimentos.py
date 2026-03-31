N = int(input())

saldo_minimo = 0
saldo = 0

for _ in range(N):
    valor = int(input())
    saldo+=valor

    saldo_minimo = min(saldo_minimo, saldo)

resposta = -saldo_minimo

print(resposta)
