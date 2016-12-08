print('Soft for guessing numbers from 1 to 5')

print("Please enter the number from 1 to 5")

a = input('Is it less then 3 (y/n):')

if a == 'y':
    b = input('Is it 1 (y/n):')
    if b != 'y':
        print('Your number is 2')
else:
    c = input('Is it 4 (y/n):')
    if c != 'y':
        d = input('Your number is 5 (y/n)?')
        if d != 'y':
            print('Your number is 3')