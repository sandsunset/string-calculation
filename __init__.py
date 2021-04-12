import re

def get_coefficient(formula:str):
    formula = formula.replace(' ','')
    variables = {}
    term = ""
    for f in formula + ';':
        variable = re.compile('(\W?[0-9]+)([a-zA-Z]+)')
        constant_term = re.compile('(\W?[0-9]+);')
        term += f

        variable = variable.match(term)
        constant_term = constant_term.match(term)
        if variable == None and constant_term == None:
            continue
        elif variable != None:
            print(variable.group(1))
            print('variable:',variable.group(2))
            term = ""
        elif constant_term != None:
            print(constant_term.group(1))
            print('constant')
            term = ""

if __name__ == '__main__':
    get_coefficient('-51i-31234')

"""
0.008~0.009
        variable = variable.match(term)
        if variable == None:
            constant_term = constant_term.match(term)
            if constant_term == None:
                continue
            else:
                print(constant_term.group(1))
                print('constant')
                term = ""
        else:
            print(variable.group(1))
            print('variable')
            term = ""


0.008~0.009
        variable = variable.match(term)
        constant_term = constant_term.match(term)
        if variable == None and constant_term == None:
            continue
        elif variable != None:
            print(variable.group(1))
            print('variable')
            term = ""
        elif constant_term != None:
            print(constant_term.group(1))
            print('constant')
            term = ""
"""