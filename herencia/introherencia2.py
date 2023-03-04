class A1: # se crea una clase nombrada (A1)
    def __init__(self): # se crea un constructor sin parametros
        pass # evita que el programa me emita un mensaje 
    def saludo(self): # se crea un metodo sin paramtros 
        print('Hola desde A1') # imprimame, hola desde A1

class A2: #se crea una clase nombrada (A2)
    def __init__(self): # se crea un constructor sin parametros
        pass # evita que el programa me emita un mensaje 
    def saludo(self): # se crea un metodo sin paramtros 
        print('Hola desde A2')  # imprimame, hola desde A2


class B(A2,A1): # se crea una clase nombrada (B) con paramtros de las 2 primeras clases 
    def __init__(self): # se crea un constructor sin parametros
        pass # evita que el programa me emita un mensaje
    def saludo(self): # se crea un metodo sin paramtros 
        print('Hola desde B') # imprimame, hola desde B
    def __str__(self): # se crea un metodo para que me devuelve una cadena de caracteres 
        return 'Soy un objeto de la clase B' # me retorna la cadena de caracteres 
obj=B() # se crea un objeto invocando la clase (B)
print(obj.__str__()) # imprimame, se llama el objeto invocando el metodo para que me devuelva la cadena de caracteres que le asigne 
#obj.saludo()
#obj.saludo()


# cad="sena"
# lista=[1,2,3]
# print(cad.__str__())
# print(lista.__str__())
