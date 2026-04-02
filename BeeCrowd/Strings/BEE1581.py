N = int(input())

for _ in range(N):
    
    K = int(input())

    idiomas = []

    for _ in range(K):
        idioma = input().strip()

        idiomas.append(idioma)
    
    if len(set(idiomas)) == 1:
        print(idiomas[0])
    else:
        print("ingles")
    
