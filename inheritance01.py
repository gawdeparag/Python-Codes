class Area:
    def measures(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(length, breadth):
        area = length * breadth
        return area

class H_area(Area):
    def __init__(self, height):
        super().measures(self, length, breadth)
        self.height = height

    def area(self, height):
        area = self.length * self.breadth * self.height
        return area

h = H_area(6)
print(h.area(5, 4))
