matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input())
        linha.append(numero)
    matriz.append(linha)
    
matriz_trans = []
for i in range(3): 
    nova_linha = []
    for j in range(3): 
        nova_linha.append(matriz[j][i])
    matriz_trans.append(nova_linha)
        
print(matriz_trans)