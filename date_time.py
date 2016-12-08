import datetime

print(datetime.datetime(2016, 11, 7, 21, 28).date())
print(datetime.date.fromtimestamp(1411111111))

#from datetime import datetime
#print(datetime.now())
print(datetime.date.today())

dt = datetime.datetime.now()
c_time = datetime.datetime(2015, 3, 24, 15, 40, 38)
delta = dt - c_time
print(delta)
delta2 = datetime.timedelta(weeks=+4)
print(delta2)

