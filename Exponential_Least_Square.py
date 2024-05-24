# import numpy as np
# from scipy.optimize import curve_fit
# import matplotlib.pyplot as plt


# def linear_ls(x_list, y_list, m):
#     sigma_x = sum(x_list)
#     sigma_y = sum(y_list)
#     sigma_x2 = sum(np.square(x_list))
#     xy = [x_list[i] * y_list[i] for i in range(len(x_list))]
#     sigma_xy = sum(xy)
#     A = np.array([[m, sigma_x], [sigma_x, sigma_x2]])
#     b = np.array([sigma_y, sigma_xy])

#     sol = list(np.linalg.solve(A, b))
#     return sol


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def exp_model(x, a, b, c):
    # y = a*np.exp(-b*(x-c)**2)
    y = a*np.exp(b*x)
    return y


# x = np.array([-8, -6, -4, -2, -1, 0, 1, 2, 4, 6, 8])
# y = np.array([99, 610, 1271, 1804, 1900, 1823, 1510, 1346, 635, 125, 24])

x = np.array([1, 1.25, 1.5, 1.75, 2])
y = np.array([5.1, 5.79, 6.53, 7.45, 8.46])

popt_exp, pcov_exp = curve_fit(exp_model, x, y)
y_fit_exp = exp_model(x, *popt_exp)
print(popt_exp)

# Plot the results
plt.scatter(x, y)
plt.plot(x, y_fit_exp, label='Exponential')
plt.legend()
plt.show()
