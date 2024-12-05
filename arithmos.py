#Ce programme est conçu afin de donner pour un nombre pair n donné la  liste  des doublons
#dont la somme des deux éléments est égale à n
#Cela permettra notamment pour un nombre pair , d'avoir la liste des doublons constitués de premier  dont il est la somme
from math import*

def est_premier(n): #Cette focntion verifie si un nombre est premier ou pas
    if(n==2):
        return True
    elif(n<2):
        return False
    else:
        reste = []
        x = int(sqrt(n))
        for k in range(2, x + 1):
            reste.append(n % k)
        reste.sort()
        if 0 in reste:
            return False
        else:
            return True
    
def dbGolb(nbr): #cette fonction renvoie la liste des doublons de Golbach pour nbr pair
    nbrd = int(nbr/2)
    if(nbr % 2 == 0):
        listn = list(range(2,nbrd+1))
    liste_tup = []
    dico= {}
    for el in listn:
        if ( est_premier(el) == True and est_premier(nbr - el) == True ):
            dico[el] = nbr - el
            liste_tup = list(dico.items())
    return len(liste_tup) , liste_tup


def primeinf(nbr):#liste des nombres premiers inférieurs à nbr
    lisPrime = []
    for num in range(nbr):
        if(est_premier(num)==True):
            lisPrime.append(num)
    print(lisPrime)


def primeEntre(a,b): #Cette renvoie la liste des nombres premiers dans un intervalle [a,b]
    lisPrime = []
    for num in range(a,b+1):
        if(est_premier(num)==True):
            lisPrime.append(num)
    print(lisPrime)

def pgcd(a,b): #Pour renvoyer  pgcd(a,b)
    print(gcd(a,b))

