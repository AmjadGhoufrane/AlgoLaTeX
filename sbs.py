
# example pour 3 + 5 * 8
example = [3, '+', 5, '*', 8]

# example = example[::-1]


def calc(arbreP):
    if not arbreP:
        return 0
        
    operators = {'+': lambda x, y: x + y, 
                 '*': lambda x, y: x * y,
                 '-': lambda x, y: x - y,
                 '/': lambda x, y: x / y
                 }
    stack = []

    


print(calc(example))