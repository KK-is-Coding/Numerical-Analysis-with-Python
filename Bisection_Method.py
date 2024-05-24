def str_to_func(expr):
    return eval("lambda x: " + expr)


def bisection(f, a, b, tol):
    if f(a) * f(b) >= 0:
        print("\nBisection method fails :(")
        return None

    c = a
    while (b-a)/2 > tol:
        c = (a+b)/2
        if f(c) == 0.0:
            break
        elif f(c)*f(a) < 0:
            b = c
        else:
            a = c
    print('\nBisection Method works :) ')
    return c


print('Enter the mathematical expression carefully : ')
expression = input()
f = str_to_func(expression)

print('Enter the initial interval in which you believe solution exist : ')
interval = list(map(int, input().split(" ")))

print('Enter the tolerence or maximum error in the solution : ')
tolerence = float(input())

# print(f(0))
# print(f(1))
output = bisection(f, interval[0], interval[1], tolerence)
print(f'Output is : {output}')
