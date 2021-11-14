import math


class Cylinder():
    def __init__(self, radius=1, height=1):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        return 2 * math.pi * (self.radius ** 2) + 2 * math.pi * self.radius * self.height


cylinder = Cylinder(2, 3)
print(cylinder.volume())
print(cylinder.surface_area())
