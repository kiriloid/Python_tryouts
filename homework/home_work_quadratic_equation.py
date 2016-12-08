def quadratic():
    a = float(input('Input a = '))
    b = float(input('Input b = '))
    c = float(input('Input c = '))

    # При его решении сначала вычисляют дискриминант по формуле D = b**2 - 4*a*c.
    # Если D > 0, то квадратное уравнение имеет два корня;
    # если D = 0, то 1 корень; и если D < 0, то делают вывод, что корней нет.

    d = b ** 2 - 4 * a * c

    if d < 0:
        print('There is no roots in this equation')
    elif d == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))

print('''This soft is intended to calculate the quadratic equation!!!
like ax**2 + bx + c = 0''')

import math

quadratic()
while True:
    rep = input('Would you like to repeat? (y/n):')
    if rep == 'y':
        quadratic()
    else:
        exit()