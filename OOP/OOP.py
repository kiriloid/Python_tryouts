class Home:
    LEVEL_3 = "Level 3"
    LEVEL_2 = "Level 2"
    LEVEL_1 = "Level 1"

parktown = Home()
level = parktown.LEVEL_1
print(level)
parktown.LEVEL_1 = "Home level 1"
print(level)
forest_town = Home()
print(forest_town)


class Home2:
    LEVEL_0 = "Level 0"

    def get_adress(self):
        print("Address 0 for this home")

