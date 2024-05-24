def gauss_elimination(A, b):
    n = len(A)

    # Augment the matrix A with the vector b
    Ab = [A[i] + [b[i]] for i in range(n)]

    # Forward elimination
    for i in range(n):

        # Find the pivot row
        pivot_row = i
        for j in range(i + 1, n):
            if abs(Ab[j][i]) > abs(Ab[pivot_row][i]):
                pivot_row = j

        # Swap the current row with the pivot row
        Ab[i], Ab[pivot_row] = Ab[pivot_row], Ab[i]

        # Eliminate the current column
        for j in range(i + 1, n):
            factor = Ab[j][i] / Ab[i][i]
            for k in range(i, n + 1):
                Ab[j][k] -= factor * Ab[i][k]

    # Backward substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i][n] / Ab[i][i]
        for j in range(i):
            Ab[j][n] -= Ab[j][i] * x[i]
    return x


m = int(input('How many unknowns are there : '))

A = [0]*m
for i in range(len(A)):
    A[i] = list(
        map(float, input(f"Enter the coefficients of equation--{i+1} : ").split(" ")))

b = [0]*m
b = list(map(float, input('Enter the solution array : ').split(" ")))

output = gauss_elimination(A, b)
print(f'\nSolutions of the system of the equations are : {output}')
