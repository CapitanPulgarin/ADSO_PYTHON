class persona:
    def __init__(self,nombre):
        self.nombre=nombre
        self.dato=[]
    def getnombre(self):
        return 'Nombre del estudiante es: ', self.nombre 
        
        
class registro:
    
    def __init__(self,id,edad, numerocontacto, nombredeusuario, contraseña):
        self.id=id
        self.edad=edad
        self.numerocontacto=numerocontacto
        self.nombredeusuario=nombredeusuario
        self.contraseña=contraseña
    
    def getid(self,identi):
        ide=persona(identi)
        self.dato.append(ide)
    
    def getnombre(self):
        return 'Nombre del estudiante es: ', self.nombre 
    
    def getedad(self):
        return 'Edad del estudiante es: ', self.edad 
    
    def getnumerocontacto(self):
        return 'Numero de contacto: ', self.numerocontacto
    
    def getnombredeusuario(self):
        return 'Nombre de usuario es: ', self.nombredeusuario
    
    def getcontraseña(self):
        return 'contraseña es: ', self.contraseña
    
ob=persona('Cesar Pulgarin')
ob.getid('1007746634')  
ob.getedad('22 años')
ob.getnumerocontacto('3122744822')
ob.getnombredeusuario('kaputbutton@gmail.com')
ob.getcontraseña('Caesar117')

print()
