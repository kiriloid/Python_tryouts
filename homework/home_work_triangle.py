print('soft for finding if a triangle can exist')

a = float(input('side A = '))
b = float(input('side B = '))
c = float(input('side C = '))

if ((a + b) > c) and ((b + c) > a) and ((a + c) > b):
    print('Triangle can exist')
else:
    print('Triangle can not exist')