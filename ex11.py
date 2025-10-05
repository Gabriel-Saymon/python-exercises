valor = int(input("Digite o valor: "))
print(f"Decompondo R$ {valor},00:")

# Usamos uma cópia do valor para não perder o valor original na impressão final
valor_restante = valor

# Verifica as notas de 100
if valor_restante >= 100:
    qtd_notas = valor_restante // 100  
    print("Quantidade de notas de 100:", qtd_notas )
    valor_restante = valor_restante % 100

if valor_restante >= 50:
    qtd_notas = valor_restante // 50
    print("Quantidade de notas de 50:", qtd_notas)
    valor_restante = valor_restante % 50

if valor_restante >= 20:
    qtd_notas = valor_restante // 20
    print("Quantidade de notas de 20:", qtd_notas)
    valor_restante = valor_restante % 20

if valor_restante >= 10:
    qtd_notas = valor_restante // 10
    print("Quantidade de notas de 10:", qtd_notas)
    valor_restante = valor_restante % 10

if valor_restante >= 5:
    qtd_notas = valor_restante // 5
    print("Quantidade de notas de 5:", qtd_notas)
    valor_restante = valor_restante % 5

if valor_restante >= 2:
    qtd_notas = valor_restante // 2
    print("Quantidade de notas de 2:", qtd_notas)
    valor_restante = valor_restante % 2
