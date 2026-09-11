class Rectangular:
    def __init__(self, width, height):
        self._width = 0
        self._height = 0

        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if not(isinstance(width, int) and (width > 0)):
            raise ValueError("Width must be an integer: {}".format(width))
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if not(isinstance(height, int) and (height > 0)):
            raise ValueError("Height must be an integer: {}".format(height))
        self._height = height

    @property
    def area(self):
        return self._width * self._height

r = Rectangular(10, 5)
r.width = 10
r.height = 5

print(r.width)
print(r.height)
print(r.area)

r.width = -100 #terá exeção aqui, pois não vai passar no if
