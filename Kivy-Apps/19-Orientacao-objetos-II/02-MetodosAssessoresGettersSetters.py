class Rectangular:
    def __init__(self, width, height):
        self.width = 0
        self.height = 0

        self.set_width(width)
        self.set_height(height)

    def set_width(self, width):
        if not(isinstance(width, int) and (width > 0)):
            raise ValueError("Width must be an integer: {}".format(width))
        self.width = width

    def set_height(self, height):
        if not(isinstance(height, int) and (height > 0)):
            raise ValueError("Height must be an integer: {}".format(height))
        self.height = height

    def get_area(self):
        return self.width * self.height

r = Rectangular(10, 5)

print(r.width)
print(r.height)
print(r.get_area())

r2 = Rectangular(-5, 5) #irá ocorrer um erro, pois vai cair na exceção do set_width, mas as linhas de cima serão executadas normalmente
