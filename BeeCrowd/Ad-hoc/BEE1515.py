while True:
    N = int(input())

    if N==0:
        break

    primeiro_envio = 9999
    planeta_enviou = ""

    for _ in range(N):
        planeta, chegada, anos_desloc = input().split()

        ano_envio = int(chegada)-int(anos_desloc)

        if ano_envio<primeiro_envio:
            primeiro_envio = ano_envio
            planeta_enviou = planeta
    
    print(planeta_enviou)

