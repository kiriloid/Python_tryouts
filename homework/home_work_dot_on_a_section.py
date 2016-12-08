x1 = float(input('Input first coordinates of a dot:'))
x2 = float(input('Input second coordinates of a dot:'))
step = float(input('Enter a step:'))

if x1 > x2:
    x1, x2 = x2, x1

print("Функция: y = -3x**2 - 4x + 20")
print('     x            y')
while x1 <= x2:
    y = -3 * x1**2 - 4 * x1 + 20
    print('\t%5.2f | %7.2f' % (x1, y))
    x1 +=step