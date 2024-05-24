import sympy


def three_end(f, x0, h):
    df = (-3*f.subs(x, x0)+4*f.subs(x, x0+h)-f.subs(x, x0+2*h))/(2*h)
    return df


def three_mid(f, x0, h):
    df = (f.subs(x, x0+h)-f.subs(x, x0-h))/(2*h)
    return df


def five_mid(f, x0, h):
    df = (f.subs(x, x0-2*h)-8*f.subs(x, x0-h) +
          8*f.subs(x, x0+h)-f.subs(x, x0+2*h))/(12*h)
    return df


def five_end(f, x0, h):
    df = (-25*f.subs(x, x0)+48*f.subs(x, x0+h)-36 *
          f.subs(x, x0+2*h)+16*f.subs(x, x0+3*h)-3*f.subs(x, x0+4*h))/(12*h)
    return df


def numerical_diff(f, points, x0, h):
    df_list = list()
    if (x0+2*h) <= (points[len(points)-1]):
        threeEnd = three_end(f, x0, h)
        df_list.append(threeEnd)
        print('3-point End-point formula is successful :)')

    if (x0+h) <= (points[len(points)-1]) and (x0-h) >= points[0]:
        threeMid = three_mid(f, x0, h)
        df_list.append(threeMid)
        print('3-point Mid-point formula is successful :)')

    if (x0+4*h) <= (points[len(points)-1]):
        fiveEnd = five_end(f, x0, h)
        df_list.append(fiveEnd)
        print('5-point End-point formula is successful :)')

    if (x0+2*h) <= (points[len(points)-1]) and (x0-2*h) >= points[0]:
        fiveMid = five_mid(f, x0, h)
        df_list.append(fiveMid)
        print('5-point Mid-point formula is successful :)')

    return df_list


def differentiation(f, x, x0):
    dF = sympy.diff(f, x)
    dFx0 = dF.subs(x, x0)
    return dFx0


expression = input("Enter the mathematical expression carefully : ")
points = list(map(float, input('Enter the points (x) : ').split(' ')))
y = list(map(float, input('Enter the values at that point (y) : ').split(' ')))
h = float(input('Enter the value of h : '))
x0 = float(input('Enter the point on which you want to find derivative : '))
x = sympy.Symbol('x')
f = sympy.sympify(expression)

output1 = numerical_diff(f, points, x0, h)
output2 = differentiation(f, x, x0)
print(output1)
print(f"f'(x0) = {output2}")
print('Errors in formulas : ')
error = [abs(item - output2) for item in output1]
print(error)
