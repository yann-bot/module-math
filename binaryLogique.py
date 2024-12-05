#Ce module contient des fonctions sur la logique binaire



def andFunction(a,b): #ET logique pour deux varibales
    if((a!=0 and a!=1) or (b!=0 and b!=1)):
        print("Les entrés doivent appartenir à l'ensemble [0,1]")
    s = 0
    if(a==1 and b==1):
        s = 1
        return s
    else:
        s = 0
        return s


def multiAndFunction(liste): #Et logique de plusieurs variables
    i=2
    k=len(liste)
    s = andFunction(liste[0],liste[1])
    while(i<k):
        s2= andFunction(s,liste[i])
        s=s2
        i=i+1
    return s


def orFunction(a,b): #Ou logique de deux variables 
    if((a!=0 and a!=1) and (b!=0 and b!=1)):
        print("Les entrés doivent appartenir à l'ensemble [0,1]")
    s = 0
    if(a==1 or b==1):
        s = 1
        return s
    else:
        s = 0
        return s


def multiOrFunction(liste): #Ou logique de plusieurs variables
    i=2
    k=len(liste)
    s = orFunction(liste[0],liste[1])
    while(i<k):
        s2= orFunction(s,liste[i])
        s=s2
        i=i+1
    return s


def xorFunction(a,b): # Ou exclusif de deux variables
    if((a!=0 and a!=1) or (b!=0 and b!=1)):
        print("Les entrés doivent appartenir à l'ensemble [0,1]")
    s = 0
    if(a==b):
        s = 0
    else:
        s = 1
    return s

def multiXorFunction(liste): # Ou exclusif de plusieurs variables&
    i=2
    k=len(liste)
    s = xorFunction(liste[0],liste[1])
    while(i<k):
        s2= xorFunction(s,liste[i])
        s=s2
        i=i+1
    return s


class HalfAdder():
    def __init__(self, a, b):
        self.e0 = a
        self.e1 = b
        self.result = 0
        self.reste = 0

    def sortie(self):
        self.result = xorFunction(self.e0,self.e1)
        return  self.result
    
    def retenue(self):
        self.retenue = andFunction(self.e0, self.)
           
        
def halfAdder(a,b):
    result = []
    s = orFunction(a,b)
    r = andFunction(a,b)
    result.append(s)
    result.append(r)
    return result

def fullAdder(a,b):
    result = []
    s = halfAdder(a,b)



