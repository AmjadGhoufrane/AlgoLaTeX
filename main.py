from arbres import *

entree = input("Entrez votre calcul : ")

def formule_vers_arbre(formule):
    formule = formule.replace(" ", "")
    if formule.isdigit():
        return noeud(int(formule), None, None)
    
    parentheses = 0
    position_operateur = -1
    for i in range(len(formule)):
        if formule[i] == '(':
            parentheses += 1
        elif formule[i] == ')':
            parentheses -= 1
        elif parentheses == 0 and formule[i] in '+-*/':
            position_operateur = i
            break
    
    if position_operateur == -1:
        if formule[0] == '(' and formule[-1] == ')':
            return formule_vers_arbre(formule[1:-1])
        return noeud(int(formule), None, None)
    
    operateur = formule[position_operateur]
    gauche = formule[:position_operateur]
    droite = formule[position_operateur+1:]
    
    return noeud(operateur, 
                 formule_vers_arbre(droite),
                 formule_vers_arbre(gauche))

arbre2 = formule_vers_arbre(entree)

arbre = noeud("+",
              noeud("*",
                    noeud(2,None,None),
                    noeud(3,None,None)),
              noeud("-",
                    noeud(5,None,None),
                    noeud(10,None,None)))


print("Arbre 1")
print(arbre.parcoursInfixe())
print("Arbre 2")
print(arbre2.parcoursInfixe())
