import random

random_integer = random.randint(0,100)

numero = int(input("Digite um numero de 0 a 100 e tente acertar o numero misterioso\n"))
acertou = 0

while(acertou == 0):
    if(numero == random_integer):
        print("Parabens!! Voce acertou!!")
        acertou = 1
    elif(numero>random_integer):
        print("O numero misterioso eh menor!")
        numero = int(input("Digite um numero de 0 a 100 e tente acertar o numero misterioso\n"))  
    elif(numero<random_integer):
        print("O numero misterioso eh maior!")
        numero = int(input("Digite um numero de 0 a 100 e tente acertar o numero misterioso\n"))
        
    