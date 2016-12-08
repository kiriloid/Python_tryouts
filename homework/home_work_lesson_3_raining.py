import time #for sleep while waiting for rain to stop

raining = input("Is it raining (y/n)?:")
if raining == 'y':
    umbrella = input('do you have an umbrella (y/n)?:')
    if umbrella == 'y':
        print('Go outside')
    else:
        while umbrella != 'y':
            print('Wait a while')
            time.sleep (0.5)
            umbrella = input('do you have an umbrella (y/n)?:')
        print('Go outside')
else:
    print('Go outside')