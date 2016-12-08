"""Enter first string: ty
Enter second string: kl;
Enter first number: 6.8
Enter second number: 8
----------
First string len more than second one: True/False
Numbers not equal to each other: True/False
First string len less than second one and numbers equal to each other: True/False
Sum of numbers more than 0: True"""

st1 = input('enter first string:')
st2 = input('enter second string:')
num1 = float(input('enter first number:'))
num2 = float(input('enter second number:'))

print(len(st1) > len(st2))
print(num1 != num2)
print((len(st1) < len(st2)) and num1 == num2)
print((num1 + num2) > 0)
