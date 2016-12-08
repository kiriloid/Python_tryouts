import string

a = input('Input any quantity of symbols or letters or digits:')

# if a is string.printable:
index = 0
while index < len(a):
    letter = a[index]
    if letter in string.ascii_lowercase:
        print('"%s" - is a lowercase letter' % letter)
    elif letter in string.ascii_uppercase:
        print('"%s" -  is a uppercase letter' % letter)
    elif letter in string.digits:
        print('"%s" - is a digit' % letter)
    elif letter in string.punctuation:
        print('"%s" - is a punctuation symbol' % letter)
    else:
        print('"%s" -  is a whitespace' % letter)
    index += 1
