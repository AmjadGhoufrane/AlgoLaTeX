import re

def latex_a_math(): # fait par Amjad Ghoufrane

    formuleLatex = input("Entrez votre formule Latex : ")

    formule = formuleLatex.strip()
    
    frac_pattern = r'\\frac\{([^{}]+)\}\{([^{}]+)\}'
    while '\\frac{' in formule:
        formule = re.sub(frac_pattern, r'(\1)/(\2)', formule)
    
    formule = formule.replace('{', '').replace('}', '')
    
    formule = re.sub(r'\((\d+)\)', r'\1', formule)
    
    return formule

# print(latex_a_math(input("Entrez votre formule Latex : ")))