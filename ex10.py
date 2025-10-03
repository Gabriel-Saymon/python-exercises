a = int(input("Digite o primeiro numero do intervalo: "))
b = int(input("Digite o ultimo numero do intervalo: "))
qtd_divisores = 0
contador = 1

print("Os primos do intervalo sao: ")

for i in range(a, b+1):
    if i <= 1:
        continue
    qtd_divisores = 0
    
    for contador in range(1, i + 1):
        
        if i % contador == 0:
            qtd_divisores += 1
            
    if qtd_divisores == 2:
        print(i)