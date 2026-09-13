class MinhaClasse:
    pass

obj = MinhaClasse()

print(type(obj)) #exibi: <class '__main__.MinhaClasse'>
print(type(MinhaClasse)) #exibi: <class 'type'>
print(obj.__class__) #exibi: <class '__main__.MinhaClasse'>
print(MinhaClasse.__class__) #exibi: <class 'type'>
print(MinhaClasse.__name__) #exibi: MinhaClasse
#print(obj.__name__) #terá erro, porque objeto não possui um nome igual a uma classe
print(obj.__class__.__name__) #exibi: MinhaClasse

MinhaClasse.var_cls = 0
print(MinhaClasse.__dict__) #exibi as propriedades/estrutura da classe. Resultado: {'__module__': '__main__','__firstlineno__': 1, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'MinhaClasse' objects>, '__weakref__': <attribute '__weakref__' of 'MinhaClasse' objects>, '__doc__': None, 'var_cls': 0}

print(obj.__dict__) #exibi as propriedades/estrutura da instância. Resultado: {}
# o objeto não mostra a variável var_cls, porque ela foi definida na classe e não na instância

print(obj.var_cls) #exibi 0, porque ele tem acesso as propriedades da classe que deu origem a instância, mas não
#mostra a propriedade no __dict__ porque não é dele, ele apenas herdou e não criou