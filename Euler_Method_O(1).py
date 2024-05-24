import numpy as np
import sympy


def euler_1(f, x0, y0, h, n):
    x = np.zeros(n+1)
    w = np.zeros(n+1)
    x[0] = x0
    w[0] = y0
    for i in range(n):
        w[i+1] = w[i] + (h*f(x[i], w[i]))
        x[i+1] = x[i] + h
        print(f'at x{i+1} = {x[i+1]}, w{i+1} = {w[i+1]}')


expression = input("(**Enter the mathematical expression carefully) y' = ")
interval = list(map(float, input('Enter the intervals : ').split(" ")))

# ~~~ when number of interval will be given ~~~
n = int(input('Enter the number of iterations : '))
h = (interval[1]-interval[0])/n

# ~~~ when h will be given ~~~
# h = float(input('Enter the value of h : '))
# n = int((interval[1]-interval[0])/h)

x0 = float(input('x0 = '))
w0 = float(input('w0 = '))
x = sympy.Symbol('x')
w = sympy.Symbol('y')
f = sympy.lambdify([x, w], expression)

euler_1(f, x0, w0, h, n)
