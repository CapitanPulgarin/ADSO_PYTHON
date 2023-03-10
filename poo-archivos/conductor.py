class Conductor: #se crea un clase
    def __init__(self,nombre,documento): # se inicializa un constructor con parametros asignados
        self.__nombre=nombre # se le asigna el atributo al parametro
        self.__documento=documento # se le asigna el atributo al parametro
    def getNombre(self): # se crea una clase 
        return self.__nombre # devuelve el valor del atributo
    def getDocumento(self): # se crea una clase
        return self.__documento # devuelve el valor del atributo
