N, M = map(int, input().split())

frutas = [input().strip().lower() for _ in range(N)]

linha = [input().strip().lower() for _ in range(M)]

for fruta in frutas:
    fruta_invert = fruta[::-1]
    achou = False

    for l in linha:
        if fruta in l or fruta_invert in l:
            achou = True
            break


    if achou:
        print(f"Sheldon come a fruta {fruta}")
    else:
        print(f"Sheldon detesta a fruta {fruta}")