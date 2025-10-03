maior = 0
menor = 0

for i in range(10):
    n = int(input())
    if(n > maior):
        maior=n
    elif(n < menor):
        menor = n

print("o maior eh: ", maior, "e o menor eh: ", menor)