import sys

for linha in sys.stdin:
    A, B, C, D = linha.split()
    print(A+B+C+D)