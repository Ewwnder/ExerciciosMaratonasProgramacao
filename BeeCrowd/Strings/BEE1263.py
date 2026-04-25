import sys

for linha in sys.stdin:
    palavras = linha.strip().split()

    contador = 0
    em_grupo = False

    for i in range(len(palavras)-1):
        atual = palavras[i][0].lower()
        prox = palavras[i+1][0].lower()

        if atual == prox:
            if not em_grupo:
                contador+=1
                em_grupo = True
        else:
            em_grupo = False
    
    print(contador)