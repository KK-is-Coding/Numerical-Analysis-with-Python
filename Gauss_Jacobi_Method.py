import numpy as np
import copy


def gauss_jacobi(A, b):
    n = len(A)
    x0 = np.array([0.0]*n)
    x = copy.deepcopy(x0)
    tolerence = 0.001
    k = 1
    while (k <= 100):
        for i in range(n):
            sum_a = 0.0
            for j in range(n):
                if j != i:
                    sum_a += float(A[i][j]*x0[j])

            x[i] = float((b[i]-sum_a)/A[i][i])

        diff = float(np.linalg.norm(x-x0)/np.linalg.norm(x))
        print(k, 'th, ieration', x)

        if (diff < tolerence):
            print('Iterations completed!')
            print(f'Solutions of the system of the equations are : {x}')
            break
        k = k+1
        x0 = copy.deepcopy(x)

    if (k >= 100):
        print('\nGauss-Jacobi Method fails :(')
    else:
        print('Gauss-Jacobi Method is successful :)')


m = int(input('How many unknowns are there : '))

A = [0]*m
for i in range(len(A)):
    A[i] = list(
        map(float, input(f"Enter the coefficients of equation--{i+1} : ").split(" ")))

b = [0]*m
b = list(map(float, input('Enter the solution array : ').split(" ")))

gauss_jacobi(A, b)
