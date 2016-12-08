size = int(input('Which size of array do you want?:'))
array = []
while len(array) <= (size-1):
    number = float(input('Please enter any number to add it into array: '))
    array.append(number)

print(array)

# for i in array:
#    if i < 0:
#       minus += 1
#       summa += i


minus = 0
summa = 0
count = 0
i = 0

while i < size:
    element = array[i]
    if element < 0:
        minus += 1
        summa += element
    count += 1
    i += 1

middle = summa / minus

minimal = min(array)
indx1 = array.index(minimal)
array[indx1] = round(middle)

print(minus, summa, middle)
print(minimal, indx1)
print(array)