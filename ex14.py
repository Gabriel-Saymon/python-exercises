n = int(input("Digite a ordem da matriz (n): "))

matriz = []


for i in range(n):
    linha_atual = []
    for j in range(n):
        if i == j:
            linha_atual.append(1)
        else:
            linha_atual.append(0)
    matriz.append(linha_atual)


print(f"\nMatriz Identidade {n}x{n}:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end="  ") 
    print()