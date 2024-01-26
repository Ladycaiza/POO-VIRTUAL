from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def thacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola me llamo: {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(aelf):
        print(f"Estoy estudianod: {self.actividad}")

dalto = Estudiante("Lucas",21,"Masculino"," Programacion")

dalto.hacer_actividad()