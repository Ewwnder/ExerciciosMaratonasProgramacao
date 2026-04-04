from collections import deque
import sys

for linha in sys.stdin:
    N = int(linha.strip())

    if N==0:
        break

    fila = deque(range(1, N+1))
    descarte = []

    while len(fila)>1:
        descarte.append(fila.popleft())
        fila.append(fila.popleft())
    
    print("Discarded cards:", end="")

    if descarte:
        print(" " + ", ".join(map(str, descarte)))
    else:
        print()
    
    print(f'Remaining card: {fila[0]}')