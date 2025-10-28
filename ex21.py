def imprimir_labirinto(labirinto, posicao_jogador):
    """
    Imprime o labirinto no console, mostrando a posição atual do jogador com um 'J'.
    """
    print("-" * 25)
    for i, linha in enumerate(labirinto):
        for j, celula in enumerate(linha):
            if (i, j) == posicao_jogador:
                print(" J ", end="")  # Posição do jogador
            elif celula == 0:
                print(" . ", end="")  # Caminho livre
            elif celula == 1:
                print(" # ", end="")  # Parede
        print() # Pula para a próxima linha
    print("-" * 25)

def ler_movimentos():
    """Lê e formata a sequência de movimentos do usuário."""
    print("\nDigite a sequência de movimentos (cima, baixo, esquerda, direita)")
    print("Exemplo: direita direita baixo baixo esquerda")
    movimentos_str = input("Movimentos: ").lower().strip()
    return movimentos_str.split()

def verificar_caminho(labirinto, inicio, fim, movimentos):
    """
    Simula o caminho do jogador e verifica se ele chega ao fim.
    """
    posicao_atual = inicio
    
    print("\nIniciando a jornada!")
    # A impressão inicial que estava aqui foi removida.

    for i, movimento in enumerate(movimentos):
        linha_atual, coluna_atual = posicao_atual
        
        # Calcula a próxima posição com base no movimento
        if movimento == 'cima':
            proxima_posicao = (linha_atual - 1, coluna_atual)
        elif movimento == 'baixo':
            proxima_posicao = (linha_atual + 1, coluna_atual)
        elif movimento == 'esquerda':
            proxima_posicao = (linha_atual, coluna_atual - 1)
        elif movimento == 'direita':
            proxima_posicao = (linha_atual, coluna_atual + 1)
        else:
            print(f"Movimento inválido '{movimento}'. Fim de jogo.")
            return False

        print(f"Passo {i+1}: Tentando mover para -> {movimento}")
        
        proxima_linha, proxima_coluna = proxima_posicao

        # --- VALIDAÇÃO DO MOVIMENTO ---

        # 1. Verificar se está fora dos limites do labirinto
        if not (0 <= proxima_linha < len(labirinto) and 0 <= proxima_coluna < len(labirinto[0])):
            print("❌ ERRO: Movimento para fora do labirinto! Você se perdeu.")
            return False

        # 2. Verificar se bateu na parede
        if labirinto[proxima_linha][proxima_coluna] == 1:
            print("❌ ERRO: Você bateu em uma parede!")
            return False
            
        # Se o movimento é válido, atualiza a posição e imprime o estado
        posicao_atual = proxima_posicao
        imprimir_labirinto(labirinto, posicao_atual)

    # --- VERIFICAÇÃO FINAL ---
    if posicao_atual == fim:
        print("\n✅ SUCESSO! Você encontrou a saída do labirinto!")
        return True
    else:
        print(f"\n❌ FALHA! Você completou os movimentos, mas não chegou à saída em {fim}.")
        print(f"Sua posição final foi {posicao_atual}.")
        return False


if __name__ == "__main__":
    # 0 = Caminho livre, 1 = Parede
    labirinto_exemplo = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]

    ponto_partida = (1, 1)  # Linha 1, Coluna 1
    ponto_saida = (4, 5)    # Linha 4, Coluna 5

    print("--- Desafio do Labirinto ---")
    print("J = Jogador, . = Caminho, # = Parede")
    print(f"Seu ponto de partida é {ponto_partida}. A saída é {ponto_saida}.")
    
    # <-- MUDANÇA PRINCIPAL AQUI -->
    # Imprime o estado inicial do labirinto ANTES de pedir os comandos do usuário.
    print("\nSeu mapa inicial é:")
    imprimir_labirinto(labirinto_exemplo, ponto_partida)

    movimentos_do_usuario = ler_movimentos()

    # Executa a simulação
    verificar_caminho(labirinto_exemplo, ponto_partida, ponto_saida, movimentos_do_usuario)