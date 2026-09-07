class Rectangular:
    def __init__(self):
        self.a = 0
        self.l = 0

    """
    Toda função/método deve ter o self para que o python passe o objeto que será manipulado
    """
    def area(self):
        return self.a * self.l

r1 = Rectangular()
r1.a = 5
r1.l = 10

print(r1.l)
print(r1.a)
print(r1.area())
