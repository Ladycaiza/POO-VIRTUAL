class Gato():
    def sonido(self):
        return "miau"
    
class Perro():
    def sonido(self):
        return "guau"

gato = Gato()
perro = Perro() 


def hacer_sonido(gato):
    print(gato.hacer_sonido())
