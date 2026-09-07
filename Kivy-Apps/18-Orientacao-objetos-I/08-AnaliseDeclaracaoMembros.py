"""
Em python, posso ir adicionando membros/propriedades ao decorrer da execução, algo parecido com o JavScript
e reflection do C#.

Só posso adicionar um novo membro adicionando um valor em tempo da declaração
"""

class Rectangular:
    def area(self):
        return self.a * self.l

def embryos_rectangular(r):
    r.a = 0
    r.l = 0

r1 = Rectangular()
embryos_rectangular(r1)
r1.a = 5
r1.l = 10

print(r1.l)
print(r1.a)
print(r1.area())
