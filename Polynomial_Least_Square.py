import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def polynomial_ls(x_list, y_list, m):
    sigma_x = sum(x_list)
    sigma_y = sum(y_list)
    sigma_x2 = sum(np.square(x_list))
    sigma_x3 = sum(np.float_power(x_list, 3))
    sigma_x4 = sum(np.float_power(x_list, 4))
    xy = [x_list[i] * y_list[i] for i in range(len(x_list))]
    sigma_xy = sum(xy)
    x2y = [(np.square(x_list[i])) * y_list[i] for i in range(len(x_list))]
    sigma_x2y = sum(x2y)

    A = np.array([[m, sigma_x, sigma_x2], [sigma_x, sigma_x2,
                 sigma_x3], [sigma_x2, sigma_x3, sigma_x4]])
    b = np.array([sigma_y, sigma_xy, sigma_x2y])

    sol = list(np.linalg.solve(A, b))
    return sol


# Define the polynomial model
# "poly_model" is a function that takes an input x and a variable number of parameters '*params'
def poly_model(x, *params):
    return np.polyval(params[::-1], x)


m = int(input('How many points are there : '))

x_list = [0]*m
x_list = list(
    map(float, input("Enter the x-coordinates of points : ").split(" ")))

y_list = [0]*m
y_list = list(
    map(float, input('Enter the y-coordinates of points : ').split(" ")))

# Get the value of constants
output = polynomial_ls(x_list, y_list, m)
print(output)


x = np.array(x_list)
y = np.array(y_list)

# Fit the polynomial model
# The resulting coefficients of the polynomial model are stored in 'popt_poly',
# and the covariance matrix of the fit is stored in 'pcov_poly'.
popt_poly, pcov_poly = curve_fit(poly_model, x, y, (1, 1, 1))
y_fit_poly = poly_model(x, *popt_poly)

# Plot the results
plt.scatter(x, y)
plt.plot(x, y_fit_poly, label='Polynomial')
plt.legend()
plt.show()
