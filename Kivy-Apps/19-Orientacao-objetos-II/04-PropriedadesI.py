class A:
    def __init__(self):
        self._var = 0

    # método privado, pois tem o _
    def _get_var(self):
        print("O valor está sendo lido")
        return self._var

    # método privado, pois tem o _
    def _set_var(self, var):
        print("O valor está sendo escrito")
        self._var = var

    # criando propriedade var que será utilizada como variável, mas que possui métodos relacionados para cada evento
    # que ocorrer (set de valor e get de valor)
    # a função é property (build property)
    var = property(_get_var, _set_var)

a = A()
a.var = 10
print(a.var)
