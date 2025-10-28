def ler_matriz_sudoku():
    matriz = []
    print("Digite os 9 números de cada linha, separados por espaço.")
    print("Exemplo para uma linha: 5 3 4 6 7 8 9 1 2")
    for i in range(9):
        while True:
            try:
                linha_str = input(f"Digite a linha {i + 1}: ").strip().split()
                if len(linha_str) != 9:
                    print("Erro: Você deve digitar exatamente 9 números. Tente novamente.")
                    continue
                
                linha_int = [int(num) for num in linha_str]
                matriz.append(linha_int)
                break  # Sai do loop while se a linha for válida
            except ValueError:
                print("Erro: Digite apenas números inteiros separados por espaço. Tente novamente.")
    return matriz

def verificar_unidade(unidade):
    """Verifica se uma lista de 9 elementos contém os números de 1 a 9 sem repetição."""
    # A forma mais eficiente: um set remove duplicatas.
    # Se a unidade for válida, seu set terá 9 elementos (1 a 9).
    return set(unidade) == {1, 2, 3, 4, 5, 6, 7, 8, 9}

def verificar_linhas(matriz):
    """Verifica se todas as linhas da matriz são válidas."""
    for linha in matriz:
        if not verificar_unidade(linha):
            return False
    return True

def verificar_colunas(matriz):
    """Verifica se todas as colunas da matriz são válidas."""
    for j in range(9):  # Itera sobre os índices das colunas
        coluna = [matriz[i][j] for i in range(9)]
        if not verificar_unidade(coluna):
            return False
    return True

def verificar_regioes(matriz):
    """Verifica se todas as regiões 3x3 da matriz são válidas."""
    # Itera sobre os cantos superiores esquerdos de cada região (0, 3, 6)
    for i_regiao in range(0, 9, 3):
        for j_regiao in range(0, 9, 3):
            regiao = []
            # Itera dentro da região 3x3
            for i in range(i_regiao, i_regiao + 3):
                for j in range(j_regiao, j_regiao + 3):
                    regiao.append(matriz[i][j])
            
            if not verificar_unidade(regiao):
                return False
    return True

def eh_sudoku_valido(matriz):
    """
    Executa todas as verificações para determinar se a solução de Sudoku é válida.
    Retorna True se todas as verificações passarem, False caso contrário.
    """
    # A função retornará True apenas se todas as verificações forem verdadeiras.
    # O 'and' em Python tem "curto-circuito": se o primeiro for falso, ele nem testa os outros.
    return verificar_linhas(matriz) and \
           verificar_colunas(matriz) and \
           verificar_regioes(matriz)

if __name__ == "__main__":
    print("--- Verificador de Solução de Sudoku ---")
    
    # Para colar uma solução válida para teste rápido:
    # 5 3 4 6 7 8 9 1 2
    # 6 7 2 1 9 5 3 4 8
    # 1 9 8 3 4 2 5 6 7
    # 8 5 9 7 6 1 4 2 3
    # 4 2 6 8 5 3 7 9 1
    # 7 1 3 9 2 4 8 5 6
    # 9 6 1 5 3 7 2 8 4
    # 2 8 7 4 1 9 6 3 5
    # 3 4 5 2 8 6 1 7 9
    
    matriz_usuario = ler_matriz_sudoku()
    
    print("\nVerificando a matriz...")
    
    if eh_sudoku_valido(matriz_usuario):
        print("\n✅ Solução de Sudoku Válida!")
    else:
        print("\n❌ Solução de Sudoku Inválida.")