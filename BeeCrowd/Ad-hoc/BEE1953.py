while True:
    try:
        
        N = int(input())

        contador_EPR = 0
        contador_EHD = 0
        contador_intrusos = 0

        for _ in range(N):
            matricula, sigla = input().split()

            if sigla == "EPR":
                contador_EPR+=1
            elif sigla == "EHD":
                contador_EHD+=1
            else:
                contador_intrusos+=1
        
        print(f'EPR: {contador_EPR}')
        print(f'EHD: {contador_EHD}')
        print(f'INTRUSOS: {contador_intrusos}')

    except EOFError:
        break