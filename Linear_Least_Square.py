import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def linear_ls(x_list, y_list, m):
    sigma_x = sum(x_list)
    sigma_y = sum(y_list)
    sigma_x2 = sum(np.square(x_list))
    xy = [x_list[i] * y_list[i] for i in range(len(x_list))]
    sigma_xy = sum(xy)
    A = np.array([[m, sigma_x], [sigma_x, sigma_x2]])
    b = np.array([sigma_y, sigma_xy])

    sol = list(np.linalg.solve(A, b))
    return sol


# Define the linear model
def linear_model(x, a, b):
    return a * x + b


m = int(input('How many points are there : '))

x_list = [0]*m
x_list = list(
    map(float, input("Enter the x-coordinates of points : ").split(" ")))

y_list = [0]*m
y_list = list(
    map(float, input('Enter the y-coordinates of points : ').split(" ")))

# Get the value of constants
output = linear_ls(x_list, y_list, m)
print(output)


x = np.array(x_list)
y = np.array(y_list)

# Fit the linear model
# The resulting coefficients of the linear model are stored in 'popt_linear',
# and the covariance matrix of the fit is stored in 'pcov_linear'.
popt_linear, pcov_linear = curve_fit(linear_model, x, y)
y_fit_linear = linear_model(x, *popt_linear)

# Plot the results
plt.scatter(x, y)
plt.plot(x, y_fit_linear, label='Linear')
plt.legend()
plt.show()
