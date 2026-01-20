Cv, Ce, Cs, Fv, Fe, Fs = map(int, input().split())

pontuacao_cormengo = Cv*3+Ce
pontuacao_flaminthians = Fv*3+Fe

if pontuacao_cormengo>pontuacao_flaminthians:
    print("C")
elif pontuacao_flaminthians>pontuacao_cormengo:
    print("F")
else:
    if Cs>Fs:
        print("C")
    elif Fs>Cs:
        print("F")
    else:
        print("=")