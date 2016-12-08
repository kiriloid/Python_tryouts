import math

diam = float(input('Введите диаметр бака:'))
height = float(input('Введите высоту бака:'))
usage = float(input('Введите расход одной банки краски на квадратные метры:'))

a = math.pi * diam**2 / 4
b = math.pi * diam * height

result = math.ceil((a*2 + b)/usage)

print('Вам потребуется купить ', result, " банки краски")

double_side = input("Хотите покрасить с внутренней стороны? (y/n):")

if double_side == 'y':
    print("В общем Вам потребуется купить ", result*2, " банок краски")
print('Спасибо за использование нашего программного обеспечения')