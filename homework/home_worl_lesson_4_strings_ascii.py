import string

a = input('Input any symbol or letter or digit, but only one:')

while a in string.printable:
    if a in string.ascii_lowercase:
        print('Your symbol is lowercase')
    elif a in string.ascii_uppercase:
        print('Your symbol is uppercase')
    elif a in string.digits:
        print('Your symbol is a digit')
    elif a in string.punctuation:
        print('Your symbol is punctuation symbol')
    else:
        print('Your symbol is whitespace')
    break