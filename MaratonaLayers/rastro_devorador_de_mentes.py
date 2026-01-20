#Exercício que no dia não conseguimos resolver, porém, após chegar em casa foi possível observar como utilizar busca binária para resolver o mesmo.
#A estratégia utilizada é calcular e ver em quais casos a distância informada é menor que o raio² proposto no exercício

import bisect

C, T = map(int, input().split())

raios = []
for _ in range(C):
    r = int(input())
    raios.append(r * r)

total_intensidade = 0

for _ in range(T):
    x, y = map(int, input().split())
    distancia = x*x + y*y 
    
    dist_calculo = bisect.bisect_left(raios, distancia)
    
    total_intensidade += (C - dist_calculo) #Aqui vou verificar em quantos casos é menor.

print(total_intensidade)
