while True:

    N = int(input())

    if N==0:
        break

    M = list(map(int, input().split()))
    L = list(map(int, input().split()))

    somaMark = sum(M)
    somaLeti = sum(L)

    trioMark = -1
    trioLeti = -1

    for i in range(N - 2):
        if M[i] == M[i+1] == M[i+2] and trioMark == -1:
            trioMark = i
        if L[i] == L[i+1] == L[i+2] and trioLeti == -1:
            trioLeti = i

    if trioMark != -1 and (trioLeti == -1 or trioMark < trioLeti):
        somaMark += 30
    elif trioLeti != -1 and (trioMark == -1 or trioLeti < trioMark):
        somaLeti += 30

    if somaMark > somaLeti:
        print("M")
    elif somaLeti > somaMark:
        print("L")
    else:
        print("T")