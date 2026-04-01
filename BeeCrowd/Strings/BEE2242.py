vogais = ['a', 'e', 'i', 'o', 'u']

risada = input().strip()

risada_vogais = ""

for c in risada:
    if c in vogais:
        risada_vogais+=c


risada_vogais_invertida = risada_vogais[::-1]

resposta = 'S' if risada_vogais_invertida == risada_vogais else 'N'

print(resposta)
