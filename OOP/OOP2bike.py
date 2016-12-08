class BIKE:
    max_speed = 40
    wheel_radius = 17
    meters_from_start = 0

    def ride(self):
        print("our bike is riding for {} meters".format(20))
        self.meters_from_start += 20

mount_bike = BIKE()
mount_bike.ride()
print(mount_bike.meters_from_start)
mount_bike.ride()
print(mount_bike.meters_from_start)
mount_bike.ride()
print(mount_bike.meters_from_start)
mount_bike.ride()
print(mount_bike.meters_from_start)
mount_bike.ride()
print(mount_bike.meters_from_start)

