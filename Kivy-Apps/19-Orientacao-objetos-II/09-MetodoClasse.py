class Bichos:
    qnt_bichos = 0

    def __init__(self):
        self.add_bicho()

    def __del__(self):
        self.del_bicho()

        if self.qnt_bichos == 0:
            print("Todos os bichos foram mortos!")

    @classmethod #deixando o método como método de classe, usando decorator
    def add_bicho(cls):
        cls.qnt_bichos += 1

    @classmethod #deixando o método como método de classe, usando decorator
    def del_bicho(cls):
        cls.qnt_bichos -= 1

    # add_bicho = classmethod(add_bicho) #deixando o método como método de classe, usando a função builtin
    # del_bicho = classmethod(del_bicho) #deixando o método como método de classe, usando a função builtin

b1 = Bichos()
print(Bichos.qnt_bichos) #exibi: 1

b2 = Bichos()
print(Bichos.qnt_bichos) #exibi: 2

b3 = Bichos()
print(Bichos.qnt_bichos) #exibi: 3

del b1
print(Bichos.qnt_bichos) #exibi: 2

del b2
print(Bichos.qnt_bichos) #exibi: 1

del b3 #exibi: Todos os bichos foram mortos!, porque o del executa o método __del__()
print(Bichos.qnt_bichos) #exibi: 0

