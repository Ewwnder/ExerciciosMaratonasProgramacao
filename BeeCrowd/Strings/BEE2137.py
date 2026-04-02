while True:
    try:

        N = int(input())

        livros = [input().strip() for _ in range(N)] #Lembrar de usar nas maratonas, economiza MUITO TEMPO, porém fica díficil converter para C++
        livros.sort()
        print("\n".join(livros))

    except EOFError:
        break