N = int(input())

hexphrase = list(input().split())

phrase = list()

for h in hexphrase:

    byte_object = bytes.fromhex(h)
    caracters = byte_object.decode('utf-8')
    
    phrase.append(caracters)

print("".join(phrase))