from matrixOperands import *
from copy import deepcopy

OPERATORS = {'+': (1, lambda x, y, mx: msum(x, y, mx)), '-': (1, lambda x, y, mx: mraz(x, y, mx)),
             '*': (2, lambda x, y, mx: mpr(x, y, mx)), '/': (2, lambda x, y, mx: mdiv(x, y, mx)),
             '^': (3, lambda x, y, mx: mpow(x, y, mx)), 
             'd': (4, lambda y, mx: mdet(y, mx)), 't': (4, lambda y, mx: mtrans(y, mx)), 'o': (4, lambda y, mx: mrev(y, mx)), 'r': (4, lambda y, mx: mrang(y, mx))}

def eval_(formula_string, allMatrixes):
    def parse(formula_string):
        number = ''
        for s in formula_string:
            if s in '1234567890.':
                number += s  
            elif number:
                yield float(number) 
                number = ''
            if s.isupper() and s.isalpha():
                yield s
            if s in OPERATORS or s in "()":
                yield s 
        if number and number[0].isdigit():
            yield float(number)  
        if not number and formula_string[-1].isupper() and formula_string[1].isalpha():
            yield formula_string[-1]

    def shunting_yard(parsed_formula):
        stack = []
        for token in parsed_formula:
            if token in OPERATORS: 
                while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                stack.append(token)
            else:
                yield token
        while stack:
            yield stack.pop()

    def calc(polish, am):
        stack = []
        for token in polish:
            #print(stack)
            if token in OPERATORS:
                if OPERATORS[token][0] < 4:
                    y, x = stack.pop(), stack.pop()
                    x, nm, flag = OPERATORS[token][1](x, y, am)
                    if flag:
                        stack.append(x)
                        am = deepcopy(nm)
                    else:
                        return ("error", {})
                else:
                    #print('!!!:: ', stack, am)
                    y = stack.pop()
                    x, nm, flag = OPERATORS[token][1](y, am)
                    if flag:
                        stack.append(x)
                        am = deepcopy(nm)
                    else:
                        return ("error", {})
            else:
                stack.append(token)
        #print(stack)
        return (stack[0], am)

    return calc(shunting_yard(parse(formula_string)), allMatrixes)   
