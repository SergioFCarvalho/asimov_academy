# Objetos e classes no Python
l = [1, 2, 3]
print(type(l))

# criando class exemplo


class Exemplo():
    pass


x = Exemplo()
print(type(x))
print("--" * 20)
# Criando classes e métodos

# ex 1


class Dog:
    def __init__(self, raca):
        self.raca = raca
        self.idade = 10
        print(f'{raca} criado(a)')

    def latir(self):
        return 'au au au'


dog = Dog("Pastor Alemão")
print(dog.idade)
print(dog.raca)
print(dog.latir())
print("--" * 20)
# Ex2


class Circle:
    def __init__(self, raio=1):
        self.raio = raio

    def calcular_area(self):
        return self.raio * self.raio * 3.14


c1 = Circle()
c2 = Circle(2)
print(c1.raio)
print(c1.calcular_area())
print(c2.raio)
print(c2.calcular_area())
print("--" * 20)

# Herança e Métodos especiais


class Animal():
    def __init__(self):
        print("Animal criado")

    def rugido(self):
        print("AAAAAAAAAAAu")

    def comendo(self):
        print("Comendo!!")


class Mostro(Animal):
    def rugido(self):
        return "ruh ruh ruh"


animal = Animal()
animal.comendo()
besta = Mostro()
print(besta.rugido())
print("--" * 20)
# Métodos especiais


class Books(object):
    def __init__(self, title, author, pages):
        print("Book created!")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return "Title%s , author:%s, pages:%s " % (self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("Books destroyed!!!")


book = Books("Curso de Python", "Prof.X", 150)
print(book)
print(len(book))
del book
