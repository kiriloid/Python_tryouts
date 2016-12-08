# input data
a = float(input("Set your height in meters:"))
b = float(input("Set your weight in kilos:"))

c = b/a**2 # weight index result
print('your weight index is: {}'.format(c))

if c >=18 and c <= 25:
    print('Normal weight range')
elif c > 25 and c <= 30:
    print('Overweight')
elif c > 30 and c <= 36:
    print('1 degree of obesity')
else:
    print('Incorrect input data')