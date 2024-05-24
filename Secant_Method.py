import sympy
import math


def secant(expression, x0, tol):
    x = sympy.Symbol('x')
    f = sympy.sympify(expression)
    xp = x0[0]
    xq = x0[1]
    fval0 = f.subs(x, xp)
    fval1 = f.subs(x, xq)
    while (abs((fval1*(xq-xp))/(fval1-fval0)) >= tol):
        fval0 = f.subs(x, xp)
        fval1 = f.subs(x, xq)

        if abs((fval1*(xq-xp))/(fval1-fval0)) < tol:
            return xq

        xtemp = xp
        xp, xq = xq, xq - ((fval1*(xq-xtemp))/(fval1-fval0))

    return None


expression = input("Enter the mathematical expression carefully : ")

tolerence = float(
    input('Enter the tolerence or maximum error in the solution : '))

x0 = list(map(float, input('Enter the initial guesses : ').split(" ")))

output = secant(expression, x0, tolerence)


if output is not None:
    print('\nSecant Method works :) ')
    print(f'Output is : {output}')
else:
    print('Secant Method fails :( ')
