class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    
pedro = Estudiante("pedro", 23, 3)

print(pedro.edad)
