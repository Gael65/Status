from entrada import Entrada
import pickle

class Agenda:
    def __init__(self):
        try:
            with open("user_data", "rb") as agenda:
                self.__entradas = pickle.load(agenda)
            agenda.close()
        except:
            self.__entradas = []

    def agregarEntrada(self, nombre, apellido, codigo, telefono, carrera):
        entrada = Entrada(nombre, apellido, codigo, telefono, carrera)
        self.__entradas.append(entrada)
        self.__doCheckpoint()

    def eliminarEntrada(self, codigo):
        if len(self.__entradas) == 0:
            return False
        else:
            index = 0
            
            for entrada in self.__entradas:
                if entrada.getCodigo() == codigo:
                    index = self.__entradas.index(entrada)
                    self.__entradas.pop(index)
                    self.__doCheckpoint()
                    return True
                    
            return False
            
    def getContactos(self):
        return self.__entradas
                
    def __doCheckpoint(self):
        #Serializar el estado del objeto (lista de contactos)
        with open("user_data", "wb") as agenda:
            pickle.dump(self.__entradas, agenda)
        agenda.close()
    