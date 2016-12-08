class Car:

    start_point = 0

    def ride_to(self, direction, miles=20):
        print("car is going to {} for {}".format(direction, miles))
        self.start_point += miles

    def get_start_point(self):
        print(self.start_point)


movement = Car()
movement.ride_to("left")
movement.get_start_point()
movement.ride_to("left")
movement.get_start_point()
movement.ride_to("left")
movement.get_start_point()
movement.ride_to("left", 50)
movement.get_start_point()

