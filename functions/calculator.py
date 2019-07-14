"""
Simple calculator without using `eval`
"""


import operator
from textwrap import dedent


MATH_OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    }


def eval_equation(equation):
    """
    Evaluate the equation
    """
    number1, opr, number2 = equation.split()
    return MATH_OPS[opr](float(number1), float(number2))


def main():
    """Calculator for simple arithmetic operations
    """
    msg = """
        Please enter an equation in the form: <num> <op> <num>
        where:
            <num> is a number such 10 or 4.5
            <op> an operator, one of +, - *, or /
        Examples:
        1 + 1
        10.5 * 3
        12.5 / 2
        Note: Spaces around the operator are needed.

        Your equation: """
    equation = input(dedent(msg))
    print(equation, '=', eval_equation(equation))


if __name__ == '__main__':
    main()
