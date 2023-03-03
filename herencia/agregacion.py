class Curso:      # se crea una clase nombrada (curso)
    def __init__(self,titulo): # se crea una funcion con el constructor con el parametro (titulo)
        self.__titulo=titulo  # se le asigna el parametro al atributo

    def getTitulo(self): # se crea un metodo llamado gettitulo sin parametro
        return self.__titulo # devuelve el valor del parametro

class Aprendiz:    # se crea una clase nombrada (aprendiz)
    def __init__(self,nombre):  # se crea un metodo 
        self.__nombre=nombre
        self.__cursos=[]

    def agregarCurso(self,nombreCursito):
        cursito=Curso(nombreCursito)
        self.__cursos.append(cursito)

    def getCursos(self):
        return self.__cursos

ap=Aprendiz('Sofia')
ap.agregarCurso('Python Basico')
ap.agregarCurso('Python Intermedio')

for c in ap.getCursos():
    print(c.getTitulo())
