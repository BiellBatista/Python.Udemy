# coding: utf-8

class A:
    """
    Construtor é um método definido implícita ou explicitamente por todas as classes e é invocado automaticamente pela máquina virtual do python.
    Todas as vezes que um objeto estiver sendo criado é por esse método que os nossos objetos serão inicializar e será esse o ponto de partida dos nossos códigos em vista de que esse método é invocado pelo pai automaticamente
    O "self" é o "this", representa o objeto sendo criado ou criado. Ou seja, o python passa a instância que está sendo criado como parametro.
    """
    def __init__(self):
        print(id(self))

def test(s):
    print(id(s))

a = A()
print(id(a))

test(a)