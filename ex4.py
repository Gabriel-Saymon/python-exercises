number = int(input())

resto = 100
div = 100
soma = 0 

while(resto != 0  and div != 0):
    soma += number%10
    resto = number%10
    
    number = (number-resto)/10
    div = number
    
print("A soma dos numeros sao:", soma)