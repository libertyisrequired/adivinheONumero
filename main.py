from auxFunctions import binarySearch, geraNumero, verificaChute, verificaInput, verificaVencedor, chutesDados
jogador = 0
vencedor = False
chuteComputador = False
pcWillPLay = verificaInput("Você quer jogar contra o computador? 1-sim/2-nao")
lim1 = verificaInput("Qual o menor número a ser gerado?")
lim2 = verificaInput("Qual o maior número a ser gerado?")
if lim1>lim2:
    print("Você digitou o limite 1 sendo o menor deles, mas já corrigimos!") 
    print("Gerando número...")
    randomNumber = int(geraNumero(lim2, lim2))
    print("Número gerado!")
else: 
    print("Gerando número...")
    randomNumber = int(geraNumero(lim1, lim2))
    print("Número gerado!")

while(not vencedor):
    if (pcWillPLay==1 and jogador==1):
        print("Vez do computador!")
        while(not chuteComputador): 
            chute = int(geraNumero(lim1, lim2))
            if(len(chutesDados)>0):
                pos = int(binarySearch(chutesDados, chute, 0, len(chutesDados)-1))
                if(chutesDados[pos]!=chute):
                    chutesDados.append(chute)
                    chuteComputador = True
                else: 
                    chuteComputador = False
            else: 
                chutesDados.append(chute)
        print("Chute do computador: " + str(chute))
        chutesDados.sort()
        chuteComputador = False
    else: 
        chute = verificaChute(lim1, lim2, "Digite qual número você acha que é: ")
    
    jogador = (jogador+1)%2
    vencedor = verificaVencedor(chute, randomNumber)
    
if (pcWillPLay==2):
    print("O Vencedor foi o jogador número: "+str(jogador+1))
    print("Parábens!!!")
else:
    if(jogador==0):
        print("O Computador venceu!!!")
    else: 
        print("Você venceu do computador!!!")