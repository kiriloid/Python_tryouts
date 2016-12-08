"""a, b = 1, 1
for i in range(1, 100):
    b, a = a, a + b
    if 10 < a < 100:
        print(a)"""

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        return F(n-1)+F(n-2)

print(F(100))
