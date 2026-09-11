class Rectangular:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangular(10, 5)
r.width = "teste"

print(r.width)
print(r.height)
print(r.area())
