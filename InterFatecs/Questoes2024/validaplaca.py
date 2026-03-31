import re

def qualPlaca(placa):
    placa = placa.strip().upper()

    if re.fullmatch(r'[AP]\d{1,5}', placa):
        return "Placa muito antiga"
    elif re.fullmatch(r'\d{1,7}', placa):
        return "Placa numerica"
    elif re.fullmatch(r'[A-Z]{2}\d{4}', placa):
        return "Placa AA-9999"
    elif re.fullmatch(r'[A-Z]{3}\d{4}', placa):
        return "Placa AAA-9999"
    elif re.fullmatch(r'[A-Z]{3}\d[A-Z]\d{2}', placa):
        return "Placa Mercosul"
    else:
        return "Placa invalida"

placa_input = input()
resultado = qualPlaca(placa_input)
print(resultado)