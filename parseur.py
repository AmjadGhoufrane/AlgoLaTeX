import re

def convert_latex_to_math():

    formuleLatex = input("Entrez votre formule Latex : ")

    formule = formuleLatex.strip()
    
    frac_pattern = r'\\frac\{([^{}]+)\}\{([^{}]+)\}'
    while '\\frac{' in formule:
        formule = re.sub(frac_pattern, r'(\1)/(\2)', formule)
    
    formule = formule.replace('{', '').replace('}', '')
    
    formule = re.sub(r'\((\d+)\)', r'\1', formule)
    
    return formule

print(convert_latex_to_math(input("Entrez votre formule Latex : ")))