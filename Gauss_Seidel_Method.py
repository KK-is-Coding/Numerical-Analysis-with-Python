import numpy as np
import copy


def gauss_seidel(A_list, b_list):
    A = np.array(A_list)
    b = np.array(b_list)
    n = len(A)
    x0 = np.array([0.0]*n)
    x = np.array(x0)
    tolerence = 0.001
    k = 1

    while (k <= 100):
        x0 = np.array(x)
        for i in range(n):
            sum_a1 = np.dot(A[i, :i], x[:i])
            sum_a2 = np.dot(A[i, i+1:], x0[i+1:])

            # x[i] = float((b[i]-sum_a1-sum_a2)/A[i][i])

            x[i] = (b[i] - sum_a1 - sum_a2) / A[i, i]

        diff = float(np.linalg.norm(x-x0)/np.linalg.norm(x))
        print(k, 'th, ieration', x)

        if (diff < tolerence):
            print('Iterations completed!')
            print(f'Solutions of the system of the equations are : {x}')
            break
        k = k+1

    if (k >= 100):
        print('Gauss-Seidel Method fails :(')
    else:
        print('Gauss-Seidel Method is successful :)')


m = int(input('How many unknowns are there : '))

A_list = [0]*m
for i in range(len(A_list)):
    A_list[i] = list(
        map(float, input(f"Enter the coefficients of equation--{i+1} : ").split(" ")))

b_list = [0]*m
b_list = list(map(float, input('Enter the solution array : ').split(" ")))

gauss_seidel(A_list, b_list)
