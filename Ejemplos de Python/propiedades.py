class Persona: #getter
    def __init__(self, nombre,edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def get_nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,new_nombre):
        self.__nombre = new_nombre
    
    @nombre.deleter
    def nombre(self,new_nombre):
        self.__nombre = new_nombre

dalto = Persona("Pepito",21)


nombre = dalto._nombre 
print(nombre)


dalto.nombre = "Pepes"


