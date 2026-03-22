V, T = map(int, input().split())

volume = V

mudancas = list(map(int, input().split()))

for m in mudancas:
    volume += m
    
    if volume>100:
        volume = 100
    if volume<0:
        volume = 0

print(volume)