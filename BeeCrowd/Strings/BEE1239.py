import sys

for linha in sys.stdin:
    linha = linha.rstrip('\n')

    i_aberto = False
    b_aberto = False
    resultado = []

    for c in linha:
        if c == '_':
            if not i_aberto:
                resultado.append('<i>')
            else:
                resultado.append('</i>')
            i_aberto = not i_aberto
        
        elif c == '*':
            if not b_aberto:
                resultado.append('<b>')
            else:
                resultado.append('</b>')
            b_aberto = not b_aberto

        else:
            resultado.append(c)
    
    print(''.join(resultado))
