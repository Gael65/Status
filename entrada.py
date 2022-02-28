class Entrada:
    def __init__(self, nombre, apellido, codigo, telefono, carrera):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__codigo = codigo
        self.__telefono = telefono
        self.__carrera = carrera

    def getNombre(self): return self.__nombre
    def getApellido(self): return self.__apellido
    def getCodigo(self): return self.__codigo
    def getTelefono(self): return self.__telefono
    def getCarrera(self): return self.__carrera
