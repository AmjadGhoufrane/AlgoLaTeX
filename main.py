from structures.arbres import *
from parseur import * 

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
        elif parentheses == 0 and formule[i] in '+-':
            position_operateur = i
            break
    
    if position_operateur == -1:
        parentheses = 0
        for i in range(len(formule)):
            if formule[i] == '(':
                parentheses += 1
            elif formule[i] == ')':
                parentheses -= 1
            elif parentheses == 0 and formule[i] in '*/':
                position_operateur = i
                break
    

    if position_operateur == -1:

        if formule[0] == '(' and formule[-1] == ')':

            return formule_vers_arbre(formule[1:-1])
        
        return noeud(int(formule), None, None)
    

    operateur = formule[position_operateur]
    gauche = formule[:position_operateur]
    droite = formule[position_operateur+1:]
    

    return noeud(operateur,formule_vers_arbre(gauche),formule_vers_arbre(droite))


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


# entree = input("Entrez votre calcul : ")
entree = latex_a_math()
arbre2 = formule_vers_arbre(entree)



print_arbre(arbre2)
print("\n"+str(arbre2.parcoursInfixe()))



