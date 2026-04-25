C = int(input())

for _ in range(C):
    mensagem_codificada = input().strip()
    mensagem_ordem = mensagem_codificada[::-1]

    mensagem_decodificada = ""

    for c in mensagem_ordem:
        if c.islower():
            mensagem_decodificada+=c
    
    print(mensagem_decodificada)