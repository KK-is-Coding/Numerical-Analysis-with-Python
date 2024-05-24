import numpy as np
import sympy


def RK_O4(f, x0, y0, h, n):
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    x[0] = x0
    y[0] = y0
    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h/2, y[i] + k1/2)
        k3 = h * f(x[i] + h/2, y[i] + k2/2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4)/6
        x[i+1] = x[i] + h
        print(f'at x{i+1} = {x[i+1]}, y{i+1} = {y[i+1]}')


expression = input("(**Enter the mathematical expression carefully) y' = ")
interval = list(map(float, input('Enter the intervals : ').split(" ")))

# ~~~ when number of interval will be given ~~~
n = int(input('Enter the number of iterations : '))
h = (interval[1]-interval[0])/n

# ~~~ when h will be given ~~~
# h = float(input('Enter the value of h : '))
# n = int((interval[1]-interval[0])/h)

x0 = float(input('x0 = '))
y0 = float(input('w0 = '))
x = sympy.Symbol('x')
y = sympy.Symbol('y')
f = sympy.lambdify([x, y], expression)

RK_O4(f, x0, y0, h, n)
