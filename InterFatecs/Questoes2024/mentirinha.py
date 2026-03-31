import math

def primo(N):
    if N<2:
        return False
    for i in range(2, int(math.sqrt(N))+1):
        if N%i==0:
            return False
    return True

def primo_mentirinha(N):
    raiz = int(math.sqrt(N))

    if raiz*raiz!=N:
        return "nao"
    
    if primo(raiz):
        return "sim"

    return "nao"

N = int(input())

resultado = primo_mentirinha(N)

print(resultado)