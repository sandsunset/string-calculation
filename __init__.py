import re

class StringCal:
    def __init__(self, formula:str):
        self.formula = formula.replace(' ', '')

    def get_coefficient(self) -> dict:
        coefficients = {}
        term = ""

        for f in self.formula + ';':
            variable_term = re.compile('(\W?[0-9]*)([a-zA-Z]+)')
            constant_term = re.compile('(\W?[0-9]+)(\W)')
            is_coefficientOne = re.compile('(\W?)([a-zA-Z]+)')
            term += f

            variable_term = variable_term.match(term)
            constant_term = constant_term.match(term)
            if variable_term == None and constant_term == None:
                continue
            elif variable_term != None:
                variable = variable_term.group(2)
                coefficient = variable_term.group(1)
                
                if is_coefficientOne.match(variable_term.group()):
                    coefficient += '1'
                try:
                    coefficients[variable] = eval(str(coefficients[variable]) + coefficient)
                except KeyError:
                    coefficients[variable] = int(coefficient)
                term = ""
            elif constant_term != None:
                constant = constant_term.group(1)
                
                try:
                    coefficients['constant'] = eval(str(coefficients['constant']) + constant)
                except KeyError:
                    coefficients['constant'] = int(constant)
                term = constant_term.group(2)

        return coefficients

if __name__ == '__main__':
    formula = StringCal('2x+1-3')
    print(formula.get_coefficient())
