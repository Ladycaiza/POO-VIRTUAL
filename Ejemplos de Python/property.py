class Persona: #getter
    def __init__(self, nombre,edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def get_nombre(self):
        return self._nombre