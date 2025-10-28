def simular_afd(cadeia):
    transicoes = {
        'S0': {'a': 'S1', 'b': 'S0'},
        'S1': {'a': 'S1', 'b': 'S2'},
        'S2': {'a': 'S1', 'b': 'S3'},
        'S3': {'a': 'S1', 'b': 'S0'}
    }
    
    estado_inicial = 'S0'
    estados_finais = {'S3'}
    alfabeto = {'a', 'b'}
    
    estado_atual = estado_inicial
    
    print("\n--- Rastreando a Execução ---")
    print(f"Estado Inicial: {estado_atual}")

    for simbolo in cadeia:
        if simbolo not in alfabeto:
            print(f"Erro: O símbolo '{simbolo}' não pertence ao alfabeto {{'a', 'b'}}.")
            return False

    for simbolo in cadeia:
        proximo_estado = transicoes[estado_atual][simbolo]
        print(f"Lendo '{simbolo}': Estado {estado_atual} -> Estado {proximo_estado}")
        estado_atual = proximo_estado

    print("----------------------------")
    
    if estado_atual in estados_finais:
        return True
    else:
        return False

if __name__ == "__main__":
    print("--- Reconhecedor de Expressão Regular: (a|b)*abb ---")
    
    # Loop para permitir múltiplos testes
    while True:
        cadeia_usuario = input("\nDigite uma cadeia de 'a's e 'b's (ou 'sair' para encerrar): ").lower()

        if cadeia_usuario == 'sair':
            break

        resultado = simular_afd(cadeia_usuario)

        if resultado:
            print(f"\n A cadeia '{cadeia_usuario}' foi ACEITA pelo autômato!")
        else:
            print(f"\n A cadeia '{cadeia_usuario}' foi REJEITADA pelo autômato.")