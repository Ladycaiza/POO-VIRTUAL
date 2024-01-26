class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor" #privado

#class MiClase:
   # def __init__(self):
       # self.__atributo__privado = "Valor" #muy muy privado
        
objeto = MiClase()
print(objeto.__hablar())