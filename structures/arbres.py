import operation
class noeud:

    def __init__(self,valeur,droite,gauche):
        self.val = valeur
        self.d = droite
        self.g = gauche

    def getValeur(self):
        return self.val
    
    def getGauche(self):
        return self.g
    
    def getDroite(self):
        return self.d
    
    def parcoursLargeur(self):
        file = [self]
        resultat =[]
        while file:

            n = file.pop(0)
            resultat.append(n.getValeur())

            if n.getDroite():
                file.append(n.getDroite())
            if n.getGauche():
                file.append(n.getGauche())
            
        return resultat

    def __repr__(self):
        return str(self.parcoursLargeur())


    def print(self):
        pass

    def parcoursLargeurRec(self):
        if (not self.d) and (not self.g) :
            return [self.val]
        if self.g and self.d :
            return [self.val,self.d.parcoursLargeurRec(),self.g.parcoursLargeurRec()]
        if self.d:
            return [self.val,self.d.parcoursLargeurRec()]
        if self.g:
            return [self.val,self.g.parcoursLargeurRec()]
        

    def taille(self):
        if (not self.d) and (not self.g) :
            return 1
        if self.g and self.d :
            return 1+self.d.taille()+self.g.taille()
        if self.d:
            return 1+self.d.taille()
        if self.g:
            return 1+self.g.taille()
        
    # retourne toutes les feuilles
    def feuilles(self):
        if (not self.d) and (not self.g) :
            return 1
        if self.g and self.d :
            return 0+self.d.feuilles()+self.g.feuilles()
        if self.d:
            return 0+self.d.feuilles()
        if self.g:
            return 0+self.g.feuilles()
        

    def parcoursInfixe(self):
        resultat = []
        if self.getGauche():
            resultat.extend(self.getGauche().parcoursInfixe())
        resultat.append(self.getValeur())
        if self.getDroite():
            resultat.extend(self.getDroite().parcoursInfixe())
        return resultat

      
    def print_arbre(node, level=0, prefix=""):
        if node is None:
            return

        space = "  "

        if node.getDroite():
            print_arbre(node.getDroite(), level + 1, "/")

        if node.getValeur() == "/":
            print(space * level + prefix + str(node.getValeur().replace("/","÷")))
        else :
            print(space * level + prefix + str(node.getValeur()))

        if node.getGauche():
            print_arbre(node.getGauche(), level + 1, "\\")
        
    def profondeur(self):
        if (not self.d) and (not self.g) :
            return 1
        if self.g and self.d :
            return 1+max(self.d.profondeur(),self.g.profondeur())
        if self.d:
            return 1+self.d.profondeur()
        if self.g:
            return 1+self.g.profondeur()

    def calculArbre(self,racine):
        if(type(self.val) != int | type(self.val) != float):
            while(self.d.profondeur() != self.g.profondeur()):
                if(self.d.profondeur() > self.g.profondeur()):
                    self.d.plusBasParent(racine)
                if(self.d.profondeur() < self.g.profondeur()):
                    self.g.plusBasParent(racine)
            if(self.d.profondeur() == self.g.profondeur()):
                self.val=operation.operation(self.val,self.d.val,self.g.val)
                self.g=None
                self.d=None
                print(racine.print_arbre);
        return self.val
