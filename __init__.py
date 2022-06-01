import time # runtime test

import re

class StringCal:
    def __init__(self, formula:str, **variables):
        self.formula = formula.replace(' ', '')
        self.variables = variables

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
                    coefficients[variable] = str(coefficients[variable]) + coefficient
                except KeyError:
                    coefficients[variable] = int(coefficient)
                term = ""
            elif constant_term != None:
                constant = constant_term.group(1)
                
                try:
                    coefficients['constant'] = str(coefficients['constant']) + constant
                except KeyError:
                    coefficients['constant'] = int(constant)
                term = constant_term.group(2)

        return coefficients
    
    def simplify(self) -> str:
        simplified_formula = ""
        no_plus_minus = re.compile('[0-9]+')
        coefficients = self.get_coefficient()

        for variable in coefficients:
            coefficient = str(coefficients[variable])

            if no_plus_minus.match(coefficient) != None and simplified_formula != '':
                coefficient = '+' + coefficient
            if variable == 'constant':
                simplified_formula += coefficient
            else:
                simplified_formula += coefficient + variable

        return simplified_formula

    def define(self, **kwargs) -> int:
        formula = self.formula
        if kwargs != {}:
            self.variables = kwargs

        for var in self.variables:
            var_value = str(self.variables[var])
            formula = formula.replace(var, '*' + var_value)

        return eval(formula)

if __name__ == '__main__':
    start = time.time()
    formula = StringCal(formula='2x+1+3x-3+3y',x=1,y=1)
    print(formula.get_coefficient())
    print(time.time() - start)
