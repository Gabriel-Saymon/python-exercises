palavra = input("Digite uma palavra ou frase para verificar: ")

palavra_formatada = palavra.lower().replace(' ', '')

palavra_invertida = palavra_formatada[::-1]

print(f"Palavra original (formatada): {palavra_formatada}")
print(f"Palavra invertida: {palavra_invertida}")

if palavra_formatada == palavra_invertida:
    print(f"\nResultado: Sim, '{palavra}' é um palíndromo!")
else:
    print(f"\nResultado: Não, '{palavra}' não é um palíndromo.")