import time
import datetime

#print(type(time.asctime()))
#print(time.clock())
#print(time.clock())
#time.daylight

print(time.gmtime().tm_hour)
print(time.localtime().tm_hour)

my_time = time.localtime()


#x, y, z = time.struct_time.tm_hour, time.struct_time.tm_min, time.struct_time.tm_sec
x, y, z = my_time.tm_hour, my_time.tm_min, my_time.tm_sec
print(x, y, z)

print(time.strftime('%d %b %Y %H:%M:%S %X  %c  %z'))
#print(time.strptime("19 November 2016 20:41", %d %b %Y %H %M))

print(time.strftime('%d_%H_%M'))


