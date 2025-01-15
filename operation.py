def operation(signe, val1, val2):
    val1 = float(val1)
    val2 = float(val2)
    
    if signe == "+":
        print(f"{val1} + {val2} = {val1 + val2}")
        return val1 + val2
    elif signe == "-":
        print(f"{val1} - {val2} = {val1 - val2}")
        return val1 - val2
    elif signe == "*":
        print(f"{val1} * {val2} = {val1 * val2}")
        return val1 * val2
    elif signe == "/":
        if val2 == 0:
            raise ValueError("Division by zero")
        print(f"{val1} / {val2} = {val1 / val2}")
        return val1 / val2
    elif signe == "^":
        print(f"{val1} ** {val2} = {val1 ** val2}")
        return val1 ** val2
    else:
        return None