class MinhaClasse:
    # membro de classe
    membro_cls = 50

    def __init__(self):
        self.membro_instancia = 0 #criando uma propriedade de instancia

    # métodos são, por padrão, da instância e não da classe, por causa do self
    def func(self):
        print("O método func() foi invocado.")
        print(MinhaClasse.membro_cls) #posso acessar um membro de classe pela classe
        print(self.membro_cls) #posso acessar um membro de classe pela instancia
        print(self.membro_instancia) #acessando o membro de instancia pelo self

i1 = MinhaClasse()
#i1.func()
#MinhaClasse.func(i1) # chamando o método func() a partir da classe, mas passando uma instância por causa do self
#MinhaClasse.func("") # chamando o método func() a partir da classe, mas passando um objeto quaisquer para atender
#a assinatura do método

i2 = MinhaClasse()

MinhaClasse.membro_cls = 10

print(i1.membro_cls) #exibi: 10
print(i2.membro_cls) #exibi: 10

print(i1.__dict__) #exibi: {'membro_instancia': 0}
print(i2.__dict__) #exibi: {'membro_instancia': 0}

i1.membro_cls = 20

"""
O comportamento que você observou acontece por causa de uma característica central do Python chamada "Shadowing" (Sombreamento) e pela forma como o Python busca variáveis nos objetos.
Quando você faz i1.membro_cls = 20, você não está alterando a variável da classe.
Em vez disso, o Python cria uma nova variável de instância exclusiva para o objeto i1, com o mesmo nome.
Ela "esconde" (sombreia) a variável da classe para aquela instância específica.

🔍 Como o Python busca as variáveis (A Regra de Escopo)
Quando você pede para ler i1.membro_cls, o Python faz uma busca em ordem:
1 - Ele olha dentro da instância (i1.__dict__). Se achar, ele usa.
2 - Se não achar na instância, ele olha dentro da classe (MinhaClasse.__dict__).

🛠️ Linha por Linha: O que está acontecendo por baixo dos panos?
Passo 1: Modificando pela Classe:

MinhaClasse.membro_cls = 10
print(i1.membro_cls) # Mostra 10
print(i2.membro_cls) # Mostra 10

- O que houve: Você alterou diretamente na classe. Como nem i1 nem i2 possuem uma variável própria chamada membro_cls, o Python foi buscar na classe e achou o valor 10 para ambos.

Passo 2: O Sombreamento (A armadilha!):

i1.membro_cls = 20

- O que houve: Em Python, o operador = em uma instância sempre cria ou atualiza um atributo na própria instância.
- Agora, o objeto i1 ganhou uma propriedade exclusiva chamada membro_cls valendo 20. A classe MinhaClasse continua valendo 10. O objeto i2 continua sem ter nada próprio.

Passo 3: Lendo após a separação:

print(i1.membro_cls) # Mostra 20
print(i2.membro_cls) # Mostra 10

- i1.membro_cls: O Python olhou primeiro na instância i1, achou o 20 que você acabou de criar e parou a busca.
- i2.membro_cls: O Python olhou na instância i2, não achou nada. Foi até a classe e pegou o 10.

Passo 4: Alterando a classe novamente:

MinhaClasse.membro_cls = 30
print(i1.membro_cls) # Mostra 20 (Independente)
print(i2.membro_cls) # Mostra 30 (Seguiu a classe)

- Como i1 agora tem sua própria cópia independente, ele ignora totalmente as mudanças na classe.
- Como i2 nunca teve um atributo próprio criado, ele continua "espelhando" o que estiver na classe.
"""

print(i1.membro_cls) #exibi: 20
print(i2.membro_cls) #exibi: 10

print(i1.__dict__) #exibi: {'membro_instancia': 0, 'membro_cls': 20}
print(i2.__dict__) #exibi: {'membro_instancia': 0}

MinhaClasse.membro_cls = 30

print(i1.membro_cls) #exibi: 20
print(i2.membro_cls) #exibi: 30

print(i1.__dict__) #exibi: {'membro_instancia': 0, 'membro_cls': 20}
print(i2.__dict__) #exibi: {'membro_instancia': 0}

"""
Para voltar a acessar a propriedade da classe a partir daquela instância depois de ter feito o sombreamento, você tem duas opções principais.

A primeira é a forma mais limpa e recomendada, enquanto a segunda desfaz o sombreamento de vez.

1. Acessando explicitamente via self.__class__ (Recomendado)
"""

print(i1.membro_cls) #exibi: 20
print(i1.__class__.membro_cls) #exibi: 30
print(i2.membro_cls) #exibi: 30

#Fora da classe, você faz o mesmo usando o nome da própria classe diretamente: MinhaClasse.membro_cls.

"""
2. Deletando o atributo da instância com del

Se você não quer apenas ler o valor da classe, mas quer que a instância i1 volte a espelhar automaticamente a classe (desfazendo o sombreamento),
você deve deletar o atributo que foi criado na instância usando a palavra-chave del.

Veja o seu exemplo modificado:

i1 = MinhaClasse()
MinhaClasse.membro_cls = 10
i1.membro_cls = 20  # Criou o sombreamento
print(i1.membro_cls) # Mostra 20
# 🔥 Removendo o sombreamento:
del i1.membro_cls  # Apaga a variável exclusiva da instância 'i1'
# Agora o Python não acha mais o atributo em 'i1' e volta a buscar na classe
print(i1.membro_cls) # Mostra 10 (Voltou a seguir a classe!)
MinhaClasse.membro_cls = 30
print(i1.membro_cls) # Mostra 30 (Continua seguindo a classe perfeitamente)

🧠 Como isso funciona por trás dos panos?

O Python guarda as variáveis de instância em um dicionário chamado __dict__.
- Quando você fez i1.membro_cls = 20, o dicionário de i1 ficou assim: {'membro_cls': 20}.
- Quando você rodou del i1.membro_cls, esse dicionário voltou a ficar vazio {}. Sem empecilhos no caminho, a busca do Python volta a subir para a classe.
"""
