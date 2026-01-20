letra_procurar = input().strip()

frase_busca = input().split()

contador_encontrado = 0

for frase in frase_busca:
    if letra_procurar in frase:
        contador_encontrado+=1

porcentagem = (contador_encontrado/len(frase_busca))*100

print(f'{porcentagem:.1f}')


