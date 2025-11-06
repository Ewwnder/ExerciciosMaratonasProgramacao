C = int(input())

foram = 0

candidatos = map(int, input().split())

for c in candidatos:
    if c == 1:
        foram+=1

print(foram)