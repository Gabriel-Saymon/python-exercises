candidatoA = 0
candidatoB = 0
nulo = 0
branco = 0
voto = 10
votosTotais = 0

while(voto != 0):
    voto = int(input("\n\tQual o seu voto?\n\n (1)CandidatoA\n (2)CandidatoB\n (3)nulo\n (4)Branco\n (0)Sair\n"))
    
    if(voto == 1):
        candidatoA += 1
    elif(voto ==2):
        candidatoB += 1
    elif(voto ==3):
        nulo += 1
    elif(voto ==4):
        branco += 1
    
    votosTotais+=1
    
votosTotais-=1
print(f"\tEstatiscas:\n")
print(f"Total de Votos: {votosTotais}\n")
print(f"Porcentagem de Votos Candidato A: {(candidatoA/votosTotais)*100}%\n")
print(f"Porcentagem de Votos Candidato B: {(candidatoB/votosTotais)*100}%\n")
print(f"Porcentagem de Votos Brancos: {(branco/votosTotais)*100}%\n")
print(f"Porcentagem de Votos Nulos: {(nulo/votosTotais)*100}%\n")
    
            
                