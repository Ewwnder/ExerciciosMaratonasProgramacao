while True:
    entrada = input().strip()

    if entrada == '*':
        print(0)
        break

    grupos = entrada.split()
    resultado = 0

    tamanho = len(grupos)

    for i in range(tamanho):
        valor = 0

        for c in grupos[i]:
            if c == '-':
                valor+=5
            elif c == '.':
                valor+=1
        
        potencia = tamanho-1-i
        resultado+=valor*(20**potencia)
    
    print(resultado)


        