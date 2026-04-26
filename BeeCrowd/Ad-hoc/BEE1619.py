def bissexto(ano):
    return (ano%400 == 0) or (ano%4 == 0 and ano%100 !=0)

def dias_valor (ano, mes, dia):
    dias = 0

    for y in range(1970, ano):
        dias+=366 if bissexto(y) else 365
    
    dias_mes = [31,28,31,30,31,30,31,31,30,31,30,31]

    for m in range(1, mes):
        if m==2 and bissexto(ano):
            dias+=29
        else:
            dias+=dias_mes[m-1]
    
    dias+=dia

    return dias

N = int(input())

for _ in range(N):
    data1, data2 = input().split()

    a1,m1,d1 = map(int, data1.split('-'))
    a2,m2,d2 = map(int, data2.split('-'))

    total1 = dias_valor(a1,m1,d1)
    total2 = dias_valor(a2,m2,d2)
    
    print(abs(total1-total2))