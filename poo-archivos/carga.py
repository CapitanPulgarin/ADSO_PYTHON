from Vehiculo import * # se importa la clase con todos sus atributos
class Carga(Vehiculo): # se crea la clase carga y tendra herencia con la clase vehiculo
    def __init__(self,placa,conductor,capacidad,ejes): # se crea un constructor con parametros asignados 
        Vehiculo.__init__(self,placa,conductor) # se instancia el constructor con sus parametros de la clase padre
        self.__capacidad=capacidad # atributo va aser igual al parametro
        self.__ejes=ejes #el atributo va a sert igual al parametro  
    def getPlaca(self): # se crea un metodo
        return self.__placa #ddevuelve el valor del atributo
    def getCapacidad(self): # se crea un metodo 
        return self.__capacidad # devuelve el valor del atributo
    def getConductor(self): # se crea un metodo
        return self.__conductor #devuelve el valor del atributo
    def getEjes(self): # se crea un metodo
        return self.__ejes #devuelve el valor del atributo
