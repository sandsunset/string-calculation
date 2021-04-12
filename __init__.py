import re

def get_coefficient(formula:str):
    variables = {}
    term = ""
    for f in formula:
        variable = re.compile('(\W?[0-9]+)([a-zA-Z])')
        constant_term = re.compile('(\W?[0-9])+\W')
        term += f

        variable = variable.match(term)
        constant_term = constant_term.match(term)
        if variable == None and constant_term == None:
            continue
        elif variable != None:
            print(variable.group(1))
            term = ""
        elif constant_term != None:
            print(constant_term.group(1))
            term = ""

if __name__ == '__main__':
    get_coefficient('-5i-3x')

"""
0.008~0.009
        variable = variable.match(term)
        if variable == None:
            constant_term = constant_term.match(term)
            if constant_term == None:
                continue
            else:
                print(constant_term.group(1))
                term = ""
        else:
            print(variable.group(1))
            term = ""


0.008~0.009
        variable = variable.match(term)
        constant_term = constant_term.match(term)
        if variable == None and constant_term == None:
            continue
        elif variable != None:
            print(variable.group(1))
            term = ""
        elif constant_term != None:
            print(constant_term.group(1))
            term = ""
"""