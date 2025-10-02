lista = list()

for i in range(5):
   lista.append(input())
   
aux = 0
   
for i in range(5):
    for j in range(5):
        if lista[i] < lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
           
print("A lista ordenada eh:", lista)
