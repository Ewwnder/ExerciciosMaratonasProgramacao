from collections import Counter

N = int(input())

notas = list(map(int, input().split()))

frequencia = Counter(notas)
maior = max(frequencia.values())

resultado = max(nota for nota, f in frequencia.items() if f == maior)

print(resultado)

