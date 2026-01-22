from collections import Counter

while True:
    try:
        N = input().strip()

        contagem = Counter(N)

        maior_frequencia = max(contagem.values())

        digito_frequente = max(digito for digito, frequencia in contagem.items() if frequencia == maior_frequencia)

        print(digito_frequente)


    except EOFError:
        break