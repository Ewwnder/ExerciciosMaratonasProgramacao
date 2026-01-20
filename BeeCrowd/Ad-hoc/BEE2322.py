N = int(input())
valores = list(map(int, input().split()))

total = set(range(1, N+1))
existentes_tabuleiro = set(valores)

falta = total-existentes_tabuleiro #Importante lembrar que é conjuntos, então aqui retorna o único que não tem entre os dois.

print(falta.pop()) #Utilizar o pop para exibir
