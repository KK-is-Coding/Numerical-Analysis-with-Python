import sympy


def fixed_point(expression, x0, tol):
    x = sympy.Symbol('x')
    f = sympy.sympify(expression)
    x_old = 0
    x_new = x0
    while (abs(x_new - x_old) > tol):
        x_old = x_new
        x_new = f.subs(x, x_old)
        if abs(x_new - x_old) < tol:
            return x_new

    return None


expression = input("Enter the mathematical expression carefully : ")

interval = list(map(float, input(
    'Enter the initial interval in which you believe solution exist : ').split(" ")))

tolerence = float(
    input('Enter the tolerence or maximum error in the solution : '))

# initial guess of x0
x0 = (interval[0]+interval[1])/2

output = fixed_point(expression, x0, tolerence)
print(f'Output is : {output}')
