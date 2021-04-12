import re

def get_coefficient(formula:str) -> dict:
    formula = formula.replace(' ','')
    coefficients = {}
    term = ""

    for f in formula + ';':
        variable = re.compile('(\W?[0-9]+)([a-zA-Z]+)')
        constant_term = re.compile('(\W?[0-9]+)[^a-zA-Z0-9_]')
        term += f

        variable = variable.match(term)
        constant_term = constant_term.match(term)
        if variable == None and constant_term == None:
            continue
        elif variable != None:
            coefficients[variable.group(2)] = variable.group(1)
            term = ""
        elif constant_term != None:
            coefficients['constant'] = constant_term.group(1)
            term = ""

    return coefficients

if __name__ == '__main__':
    print(get_coefficient('2  x        -3+     5  x + 4                 '))
