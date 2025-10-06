import random

palavras = ["casa", "rua", "carro", "bicicleta", "apartamento"]
palavra_da_vez = random.choice(palavras)
tamanho = len(palavra_da_vez)

palavra_oculta = ["_"] * tamanho

# print(f"A palavra escolhida foi: {palavra_da_vez}")

print("Bem vindo ao jogo da Forca! Você tem apenas 5 erros... Boa sorte!\n")

erros = 0
letras_acertadas = 0
fim_de_jogo = 0

while not fim_de_jogo: 
    
    print("Palavra: " + " ".join(palavra_oculta))
    print(f"Erros cometidos: {erros}/5")
    
    letra = input("\nDigite uma letra: ").lower()
    
    letra_encontrada = False 
    
    for indice, letra_na_palavra in enumerate(palavra_da_vez):
        
        if letra == letra_na_palavra:
            palavra_oculta[indice] = letra
            letra_encontrada = True
            
    if not letra_encontrada:
        erros += 1
        print(f"A letra '{letra}' não está na palavra.")
        
    if "_" not in palavra_oculta:
        print("\n" + "".join(palavra_oculta))
        print("Parabéns, você venceu!")
        fim_de_jogo = 1
        
    elif erros >= 5:
        print("\nVocê perdeu! A palavra era:", palavra_da_vez)
        fim_de_jogo = 1