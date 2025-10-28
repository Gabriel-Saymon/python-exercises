def ler_matriz_3x3():
    matriz = []
    print("--- Digite os elementos da Matriz 3x3 ---")
    for i in range(3):
        linha = []
        for j in range(3):
            while True:
                try:
                    # Pede um número para a posição [i+1, j+1]
                    numero = float(input(f"Digite o elemento da posição [{i+1}][{j+1}]: "))
                    linha.append(numero)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
        matriz.append(linha)
    return matriz

def calcular_determinante_3x3(matriz):
    a, b, c = matriz[0][0], matriz[0][1], matriz[0][2]
    d, e, f = matriz[1][0], matriz[1][1], matriz[1][2]
    g, h, i = matriz[2][0], matriz[2][1], matriz[2][2]

    soma_positiva = (a * e * i) + (b * f * g) + (c * d * h)

    soma_negativa = (g * e * c) + (h * f * a) + (i * d * b)

    determinante = soma_positiva - soma_negativa
    
    return determinante

if __name__ == "__main__":

    matriz_usuario = ler_matriz_3x3()
    print("\nMatriz inserida:")
    for linha in matriz_usuario:
        print(f"[{linha[0]:>8.2f} {linha[1]:>8.2f} {linha[2]:>8.2f}]")

    resultado = calcular_determinante_3x3(matriz_usuario)
    
    print(f"\nO determinante da matriz é: {resultado}")