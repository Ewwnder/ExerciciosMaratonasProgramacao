while True:
    try:

        enigma = input().strip()

        parte1, resultado = enigma.split("=")
        termo1, termo2 = parte1.split("+")

        if termo1.isalpha():
            valor = int(resultado)-int(termo2)
        elif termo2.isalpha():
            valor = int(resultado)-int(termo1)
        elif resultado.isalpha():
            valor = int(termo1)+int(termo2)

        print(valor)

    except EOFError:
        break