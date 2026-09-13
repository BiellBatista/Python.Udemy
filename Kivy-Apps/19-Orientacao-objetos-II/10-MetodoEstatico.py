"""
Um método estático em Python é uma função comum agrupada dentro de uma classe para fins de organização, definida com o decorador @staticmethod,
- Sem acesso a estado: ele não sabe nada sobre a instância do objeto (self) ou sobre a classe (cls).
- Comportamento: funciona exatamente como uma função livre, mas fica dentro do escopo da classe por ter relação lógica com ela.que não recebe nem o objeto (self) nem a classe (cls) como argumento automático.
- Como chamar: pode ser chamado diretamente pela classe ou por uma instância dela.

Diferença entre Método Estático e Método de Classe

A principal diferença está no acesso ao contexto da classe e no uso de argumentos implícitos.
| Característica        | Método Estático (@staticmethod)                       | Método de Classe (@classmethod)                                   |
| Argumento implícito   | Nenhum (self ou cls ausentes).                        | Recebe a classe como primeiro argumento (cls).                    |
| Acesso a dados        | Não acessa nem modifica dados da classe ou instância. | Pode acessar e modificar atributos e estado da classe.            |
| Uso principal         | Funções utilitárias ou auxiliares isoladas.           | Construtores alternativos ou operações que dependem da classe.    |
"""

class MetodoEstatico:
    @staticmethod #deixando o método como método estático, usando decorator
    def func1():
        print("func1()")

    @staticmethod #deixando o método como método estático, usando decorator
    def func2(x, y):
        print("func2({}, {})".format(x, y))

    @staticmethod #deixando o método como método estático, usando decorator
    def func3(a, b, c):
        info = """
        Nome da função: {nome}
        Quantidade de argumentos: {quantidade}
        Argumentos: {argumentos}
        """

        info = info.format(
            nome=MetodoEstatico.func3.__name__,
            quantidade=MetodoEstatico.func3.__code__.co_argcount,
            argumentos=MetodoEstatico.func3.__code__.co_varnames)

        print(info)

    # func1 = staticmethod(func1) #deixando o método como método estático, usando a função builtin
    # func2 = staticmethod(func2) #deixando o método como método estático, usando a função builtin
    # func3 = staticmethod(func3) #deixando o método como método estático, usando a função builtin

me = MetodoEstatico()

me.func1() #exibi: func1()
MetodoEstatico.func1()  #exibi: func1()

me.func2(100, 200) #exibi: func2(100, 200)
MetodoEstatico.func2(300, 400)  #exibi: func2(100, 200)

me.func3(100, 200, 300) #exibi: Nome da função: func3 Quantidade de argumentos: 3 Argumentos: ('a', 'b', 'c', 'info') O info apareceu, porque o co_varnames lista todas as variaveis do método, tanto parametro quanto definida ao decorrer do escopo
MetodoEstatico.func3(400, 500, 600)  #exibi: Nome da função: func3 Quantidade de argumentos: 3 Argumentos: ('a', 'b', 'c', 'info') O info apareceu, porque o co_varnames lista todas as variaveis do método, tanto parametro quanto definida ao decorrer do escopo
