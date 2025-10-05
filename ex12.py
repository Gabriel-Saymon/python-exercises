num = int(input("Qual o numero deseja saber o seu fatorial? "))
mult=1

for i in range(1, num+1):
    mult = mult*i
    
print("O fatorial de", num, "eh", mult)