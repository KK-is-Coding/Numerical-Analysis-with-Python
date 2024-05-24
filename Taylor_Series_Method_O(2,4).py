# taylor order 2,4
import matplotlib as plt
from scipy.optimize import curve_fit
import numpy as np


def f(x, y):
    # return np.cos(x) + np.sin(y)
    return x**2 + y**2


def f1(x, y):
    # return -np.sin(x) + np.cos(x)*np.cos(y) + np.sin(y)*np.cos(y)
    return 2*x + 2*y*(x**2+y**2)


# def f2(x, y):
#     return (-2+x-y)/8


# def f3(x, y):
#     return (2-x+y)/16


def SOTSM(a, b, x0, y0, h):
    x_list = []
    y_list = []
    while b > a:
        y1 = y0 + h*f(x0, y0) + ((h**2)/2)*f1(x0, y0)
        x0 = x0+h
        y0 = y1
        print("Value of y at x= %0.4f" % x0, " is %0.4f " % y0)
        x_list.append(x0)
        y_list.append(y0)
        b = b-h
    return x_list, y_list


# def FOTSM(a, b, x0, y0, h):
#     while b > a:
#         y1 = y0 + h*f(x0, y0) + ((h**2)/2)*f1(x0, y0) + \
#             ((h**3)/6)*f2(x0, y0) + ((h**4)/24)*f3(x0, y0)
#         x0 = x0+h
#         y0 = y1
#         print("Value of y at x= %0.4f" % x0, " is %0.4f " % y0)
#         b = b-h


print("Enter the range.")
a = float(input("From : "))
b = float(input("To : "))
x0 = float(input("Enter value of x0: "))
y0 = float(input("Enter value of y0: "))

# N = float(input("Enter intervals: "))
# h = (b-a)/N

h = float(input('Enter the step length : '))


# taylor 2nd order
print("\nTaylor 2nd order \n")
x_list, y_list = SOTSM(a, b, x0, y0, h)

# taylor 4nd order
# print("\nTaylor 4th order \n")
# FOTSM(a, b, x0, y0, h)
x = np.array(x_list)
y = np.array(y_list)

popt, pcov = curve_fit(f, x, y)
y_fit_linear = (x, *popt)

# Plot the results
plt.scatter(x, y)
plt.plot(x, y, label='ODE Solution')
plt.legend()
plt.show()
