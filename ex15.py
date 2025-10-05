qtd_notas = int(input("Digite a quantidade de notas a serem lidas: "))
soma = float()

for i in range(qtd_notas):
    nota= float(input(f"Digite a nota {i+1}: "))
    peso= float(input(f"Digite o peso da nota {i+1}: "))
    nota= nota*peso
    soma+=nota
    
media = soma/qtd_notas
print("A media do aluno eh:", media)
    