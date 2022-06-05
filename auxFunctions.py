import random

chutesDados = []

def geraNumero(lim1, lim2): 
    n = int(random.randint(lim1, lim2))
    return n

def verificaInput(msg): 
    print(msg)
    try: 
        n = int(input())
        return n
    except:
        print("Digite um número!")
        return verificaInput(msg)

def verificaChute(lim1, lim2, msg):
    n = verificaInput(msg)
    if (n < lim1 or n > lim2): 
        print("Você digitou um número fora dos limites!")
        return verificaInput(msg)
    return n 

def verificaVencedor(chute, randomNum):
    if(chute==randomNum): 
        return True
    else:
        return False

def binarySearch(chutesDados, n, pi, pf):
    if(pi==pf): 
        return pi
    m = int((pi+pf)/2)
    if(n>chutesDados[m]):
        return binarySearch(chutesDados, n, m+1, pf)
    return binarySearch(chutesDados, n, pi, m)