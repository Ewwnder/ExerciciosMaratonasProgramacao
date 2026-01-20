N = int(input())

indicadores_fila = list(map(int, input().split()))

M = int(input())

indicadores_deixaram_fila = list(map(int, input().split()))

for indicador in indicadores_deixaram_fila:
    indicadores_fila.remove(indicador)
    

print(*indicadores_fila)