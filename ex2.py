palavra = str(input())
count = 0

for i in range(len(palavra)):
    if(palavra[i] == "a" or palavra[i] == "A"):
        count+=1
    elif(palavra[i] == "e" or palavra[i] == "E"):
        count+=1
    elif(palavra[i] == "i" or palavra[i] == "I"):
        count+=1
    elif(palavra[i] == "o" or palavra[i] == "O"):
        count+=1
    elif(palavra[i] == "u" or palavra[i] == "U"):
        count+=1


print("A quantidade de vogais sao: ", count)
    