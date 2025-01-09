

class Maillon :
        def __init__(self,valeur,suiv):
            self.tete = True
            self.valeur = valeur
            self.suivant = suiv

        def getValeur(self):
            return self.valeur
        
        def getSuivant(self):
            return self.suivant
        
        def getElement(self,index):
            i = 0
            act = self
            while act.suiv != None and i<=index :
                act = self.suiv
            return act.getValeur
        
        def isTete(self):
            return self.tete

class Pile :

    def __init__(self):
        self.maillon = Maillon(None,None)
        self.tete = self.maillon

    def empiler(self,valeur):
        actu = self.maillon
        while actu.suivant != None :
            actu = actu.suivant
        if actu.valeur == None :
            actu.valeur = valeur
        elif actu.suivant == None :
            ntete = Maillon(valeur,None)
            actu.suivant = ntete
            self.tete = ntete

    def depiler(self) :
        prec = None
        actu = self.maillon    
        while actu.suivant != None :
            prec = actu
            actu = actu.suivant
        if prec == None :
           ret = actu.getValeur()
           actu.valeur = None
           return ret
        prec.suivant = None
        self.tete = prec
        return actu.getValeur()
    
    def getTete(self):
        return self.tete.getValeur()
    
    def trier(self):
        actu = self.maillon
        while actu.suivant != None:
            comp = actu.suivant
            while comp != None:
                if comp.valeur != None and actu.valeur != None and comp.valeur < actu.valeur:
                    temp = actu.valeur
                    actu.valeur = comp.valeur
                    comp.valeur = temp
                comp = comp.suivant
            actu = actu.suivant
    
    def __repr__(self):
        ret = "["
        actu = self.maillon
        while actu.suivant != None :
            ret = ret+str(actu.valeur)+","
            actu = actu.suivant
        if actu.valeur == None :
            ret = ret +"]"
        else :
            ret = ret + str(actu.valeur)+"]"
        return ret


p1 = Pile()
p1.empiler(1)
p1.empiler(3)
p1.empiler(2)
print(p1.getTete())
print(p1)
p1.trier()
print(p1)
print(p1.depiler())
print(p1)
print(p1.depiler())
print(p1)
print(p1.depiler())
print(p1)