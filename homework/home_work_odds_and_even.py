a=int(input('Enter any number:'))

even = 0
odd = 0

for i in range(a):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
    #a = a // 10

print("Even: %d, odd: %d" % (even, odd))