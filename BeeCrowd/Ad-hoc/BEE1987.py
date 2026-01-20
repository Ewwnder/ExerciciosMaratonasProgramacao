while True:
    try:
        n, m = map(int, input().split())

        soma_digitos = 0

        for numero in str(m):
            soma_digitos+=int(numero)
        
        if soma_digitos%3==0:
            print(f'{soma_digitos} sim')
        else:
            print(f'{soma_digitos} nao')

    except EOFError:
        break