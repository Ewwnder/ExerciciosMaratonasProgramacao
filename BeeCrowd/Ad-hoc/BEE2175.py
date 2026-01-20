import sys

for linha in sys.stdin:
    linha = linha.strip()
    
    if not linha:
        continue

    
    O, B, I = map(float, linha.split())

    tempos = { #Importante levar nas maratonas.
        "Otavio": O,
        "Bruno": B,
        "Ian": I
    }

    menor_tempo = min(tempos.values()) #Importante levar e usar nas maratonas, agiliza muito na hora de achar o menor ou maior.

    vencedor = [nome for nome, tempo in tempos.items() if tempo == menor_tempo]

    if len(vencedor)>1:
        print("Empate")
    else:
        print(vencedor[0])

