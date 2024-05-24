import numpy as np


def lagrange_interp(x, y, z):
    n = len(x)
    result = 0
    for j in range(n):
        L = 1
        for i in range(n):
            if i != j:
                L *= (z - x[i]) / (x[j] - x[i])
        result += y[j] * L

    return result


m = int(input('How many points are there : '))

x_list = [0]*m
x_list = list(
    map(float, input("Enter the x-coordinates of points : ").split(" ")))

y_list = [0]*m
y_list = list(
    map(float, input('Enter the y-coordinates of points : ').split(" ")))


x = np.array(x_list)
y = np.array(y_list)

# Interpolate the value of y at x
z = float(input('Enter the value of x for which you want to get value of y : '))
output = lagrange_interp(x, y, z)
print(f'\nat x = {z}, y = {output}')
