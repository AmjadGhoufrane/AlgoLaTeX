def operation(signe,val1,val2):
    if signe == "+":
        print(val1+" + "+val2+" = "+val1 + val2)
        return val1 + val2
    elif signe == "-":
        print(val1+" - "+val2+" = "+val1 - val2)
        return val1 - val2
    elif signe == "*":
        print(val1+" * "+val2+" = "+val1 * val2)
        return val1 * val2
    elif signe == "/":
        print(val1+" / "+val2+" = "+val1 / val2)
        return val1 / val2
    elif signe == "^":
        print(val1+" ** "+val2+" = "+val1 ** val2)
        return val1 ** val2
    else:
        return None