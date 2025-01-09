from pile import *
from timer_deco import *
from random import *

class File:
    def __init__(self):
        self.maillon = Maillon(None, None)
        self.fin = self.maillon

    def enfiler(self, valeur):
        if self.maillon.valeur is None:
            self.maillon.valeur = valeur
        else:
            nouveau = Maillon(valeur, None)
            self.fin.suivant = nouveau
            self.fin = nouveau

    def defiler(self):
        if self.maillon.valeur is None:
            return None
        valeur = self.maillon.valeur
        if self.maillon.suivant is None:
            self.maillon.valeur = None
            self.fin = self.maillon
        else:
            self.maillon = self.maillon.suivant
        return valeur

    def getFin(self):
        return self.fin.getValeur()

    def trier(self):
        elements = []
        while self.maillon.valeur is not None:
            elements.append(self.defiler())
        elements.sort()
        for element in elements:
            self.enfiler(element)

    def __repr__(self):
        ret = "["
        actu = self.maillon
        while actu.suivant is not None:
            ret = ret + str(actu.valeur) + ","
            actu = actu.suivant
        if actu.valeur is None:
            ret = ret + "]"
        else:
            ret = ret + str(actu.valeur) + "]"
        return ret



f = File()
#for i in range (5000):
#    f.enfiler(randint(0,5000))
f.enfiler(2)
f.enfiler(1)
f.enfiler(3)
print(f)
f.trier()
print(f)
print(f.defiler())
print(f)
print(f.defiler())
print(f)
print(f.defiler())
print(f)