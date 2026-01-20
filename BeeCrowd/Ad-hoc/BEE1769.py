while True:
    try:
        cpf = input().strip().replace('.', '').replace('-', '')

        digito = [int(c) for c in cpf]

        if len(digito)!=11:
            print("CPF invalido")
            continue

        soma1 = 0

        for i in range(9):
            soma1 += digito[i]*(i+1)
        
        base1 = soma1%11
        if base1 == 10:
            base1 = 0
        
        soma2 = 0

        for i in range(9):
            soma2 += digito[i]*(9-i)
        
        base2 = soma2%11
        if base2 == 10:
            base2 = 0
        
        if base1 == digito[9] and base2 == digito[10]:
            print("CPF valido")
        else:
            print("CPF invalido")

    except EOFError:
        break