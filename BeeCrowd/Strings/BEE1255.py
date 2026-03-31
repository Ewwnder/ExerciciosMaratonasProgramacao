from collections import Counter

N = int(input())

for _ in range(N):
    frase = input().lower()

    filtro_letras = [c for c in frase if c.isalpha()]

    frequencia_letras = Counter(filtro_letras)
    maior = max(frequencia_letras.values())

    letras = [letra for letra, freq in frequencia_letras.items() if freq == maior]

    letras.sort()

    resultado = ''.join(letras)

    print(resultado)