import math

def primo(N):
    if N<2:
        return False
    for i in range(2, int(math.sqrt(N))+1):
        if N%i==0:
            return False
    return True

def verificar_super_primo(N):
    for digito in str(N):
        if int(digito) not in [2,3,5,7]:
            return False
    return True

while True:
    try:
        N = int(input())

        if not primo(N):
            print("Nada")
        else:
            if verificar_super_primo(N):
                print("Super")
            else:
                print("Primo")
    except EOFError:
        break