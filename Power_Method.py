import numpy as np


def power(A_list, x0_list, max_iter):
    A = np.array(A_list)
    x0 = np.array(x0_list)
    x = np.array(x0)
    tol = 0.0001

    for i in range(max_iter):
        # matrix multiplication
        y = np.dot(A, x)

        # normalization and finding eiganvalue
        eigenvalue = np.linalg.norm(y, np.inf)
        x = y / eigenvalue

        # checking the convergence criteria
        if np.linalg.norm(np.dot(A, x) - (eigenvalue * x), np.inf) < tol:
            break
    return eigenvalue, x


m = int(input('Enter the number of rows or columns in matrix : '))

A_list = [0]*m
for i in range(len(A_list)):
    A_list[i] = list(
        map(float, input(f"Enter the numbers in the row--{i+1} : ").split(" ")))

x0_list = [0]*m
x0_list = list(
    map(float, input('Enter the initial guess for the eiganvector : ').split(" ")))

max_iteration = int(input('How many iterations do you want : '))

ouput = power(A_list, x0_list, max_iteration)
print(
    f'\nSo, the largest eiganvalue is {ouput[0]} and the corresponding eiganvector is {ouput[1]}')
