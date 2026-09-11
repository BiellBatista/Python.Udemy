class A:
    def __init__(self):
        self._var = 0

    # @property indica que o método é de get
    @property
    def var(self):
        print("O valor está sendo lido")
        return self._var

    # @nomeDaProriedade.setter indica que o método é de set
    @var.setter
    def var(self, var):
        print("O valor está sendo escrito")
        self._var = var

a = A()
a.var = 5
print(a.var)
