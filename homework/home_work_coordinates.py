print('Софт для нахождения в какой четверти координатной оси находиться точка')

#I-й четветри соответствуют точки, имеющие обе (x и y) положительные координаты.
#II-ая четверть: x < 0, y > 0.
#III-ая четверть: x < 0, y < 0.
#IV-ая четверть: x > 0, y < 0.

x = float(input('Введите координаты точки по оси х: '))
y = float(input('Введите координаты точки по оси y: '))

if x > 0 and y > 0:
    print('Dot is in the I quarter')
elif x < 0 and y > 0:
    print('Dot is in the II quarter')
elif x < 0 and y < 0:
    print('Dot is in the III quarter')
elif x > 0 and y < 0:
    print('Dot is in the IV quarter')