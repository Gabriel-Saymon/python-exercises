def converter_numeros_romanos(numeroNormal):
    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    
    numeroRomano = ""
    
    for valor, simbolo in valores:
        while numeroNormal >= valor:
            numeroRomano += simbolo
            numeroNormal -= valor
            
    return numeroRomano


while(1):
    numeroNormal = int(input("Digite um número inteiro entre 1 e 3999: "))
    
    if(numeroNormal >= 1 and numeroNormal <= 3999):
        break
    else:
        print("Numero invalido.\n")
        

romano = converter_numeros_romanos(numeroNormal)
print(f"O número {numeroNormal} em algarismos romanos é: {romano}")
