import math


class Line():
    def __init__(self, coordinate1, coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2

    def distance(self):
        x1, y1 = self.coordinate1
        x2, y2 = self.coordinate2
        return (((x2-x1) ** 2) + ((y2-y1) ** 2)) ** 0.5

    def slope(self):
        x1, y1 = self.coordinate1
        x2, y2 = self.coordinate2
        return (y2-y1)/(x2-x1)


c1 = (3, 2)
c2 = (8, 10)
line = Line(c1, c2)
print(line.distance())
print(line.slope())
