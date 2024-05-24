import sympy
import math
# import pylab
# import numpy


def new_raph(expression, x0, tol):
    x = sympy.Symbol('x')
    f = sympy.sympify(expression)
    df = sympy.diff(f, x)
    xn = x0
    fval = f.subs(x, xn)
    dfval = df.subs(x, xn)
    while (abs(fval/dfval) >= tol):
        fval = f.subs(x, xn)
        dfval = df.subs(x, xn)

        if abs(fval/dfval) < tol:
            return xn

        xn = xn - fval/dfval

    return None


expression = input("Enter the mathematical expression carefully : ")

tolerence = float(
    input('Enter the tolerence or maximum error in the solution : '))

x0 = float(input('Enter the initial guess : '))

output = new_raph(expression, x0, tolerence)
if output is not None:
    print('\nNewton-Raphson Method works :) ')
    print(f'Output is : {output}')
else:
    print('Newton-Raphson Method fails :( ')
