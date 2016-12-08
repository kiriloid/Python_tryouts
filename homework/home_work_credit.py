import time, sys

s = float(input('Сколько Вы хотите взять долларов в качестве займа?:'))
n = float(input('На сколько лет Вы хотите продаться в каббалу?:'))
p = (float(input('Какой процент банка?:')))/100

m = (s * p * (1 + p)**n) / (12 * ((1 + p)**n - 1))
result = m * 12 * n

print('Идёт процесс вычисления:')
i = 0
while i<6:
    sys.stdout.write("\r%0.2i"%(i))
    sys.stdout.flush()
    i+=1
    time.sleep(0.5)

print('')
print('Сумма Вашей ежемесячной выплаты равна: %.2f долларов' %m)
print('И в итоге Вы заплатите: %.2f долларов' %result)