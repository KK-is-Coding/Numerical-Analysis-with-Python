import sympy
import numpy as np
import scipy


def trapezoidal(y, h):
    integral_f = ((y[0]+y[-1])/2 + np.sum(y[1:-1]))*h
    return integral_f


def simpson_1by3(y, h):
    integral_f = h*(y[0] + y[-1] + 4*np.sum(y[1:-1:2]) +
                    2*np.sum(y[2:-1:2]))/3
    return integral_f


def simpson_3by8(y, h):
    integral_f = (3*h*(y[0] + y[-1] + 3*np.sum(y[1:-1:3]) + 3 *
                       np.sum(y[2:-1:3]) + 2*np.sum(y[3:-1:3])))/8
    return integral_f


def numerical_integration(f, interval, n, h):
    points = []
    y = []
    res = []
    for i in range(n+1):
        points.append(interval[0]+i*h)
        y.append(f.subs(x, points[i]))

    res.append(trapezoidal(y, h))
    print('Trapezoidal method is successful :)')

    if n % 2 == 0:
        res.append(simpson_1by3(y, h))
        print('Simpson 1/3 method is successful :)')

    if n % 3 == 0:
        res.append(simpson_3by8(y, h))
        print('Simpson 3/8 method is successful :)')

    return res


expression = input("Enter the mathematical expression carefully : ")
interval = list(map(float, input('Enter the intervals : ').split(" ")))
n = int(input('Enter the number of subinterval : '))
h = (interval[1]-interval[0])/n
x = sympy.Symbol('x')
f = sympy.sympify(expression)


output1 = numerical_integration(f, interval, n, h)
# output2 = integration(f, x, interval)
output2 = float(sympy.integrate(f, (x, interval[0], interval[1])))
print(output1)
print(f"Sf(x) = {output2}")
print('Errors in formulas : ')
error = [abs(item - output2) for item in output1]
print(error)
