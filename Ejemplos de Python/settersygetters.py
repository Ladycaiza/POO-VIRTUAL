class Persona: #getter
    def __init__(self, nombre,edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre
    
dalto = Persona("Pepito",21)

nombre = dalto.get_nombre()
print(nombre)


