
class register:
    def __init__ (self,id,nombre,edad,num_conta,nom_usu,contraseña):
        self.id=id
        self.nombre=nombre
        self.edad=edad
        self.num_conta=num_conta
        self.nom_usu=nom_usu
        self.contraseña=contraseña

    
    def agrid(self):
        return self.id
    def agrnombre(self):
        return self.nombre
    def agredad(self):
        return self.edad
    def agrnum_tel(self):
        return self.num_conta   
    def agrnom_usu(self):
        return self.nom_usu
    def agrclave(self):
        return self.contraseña
    
class instructor(register):
    def __init__(self,Usu_nom,Cla_instructor):
        self.Usu_nom=Usu_nom
        self.Cla_istructor=Cla_instructor

    def getN_inst(self):
        return self.Usu_nom
    
    def getC_inst(self):
        return self.Cla_istructor

class transaciones:
    def __init__ (self,T_ident,T_Detalles,T_fecha,mediopago):
        self.T_ident=T_ident
        self.T_Detalles=T_Detalles
        self.T_fecha=T_fecha
        self.mediopago=mediopago
    def agregaID(self):
        return self.T_ident
    def agregaDET(self):
        return self.T_Detalles
    def agregafecha(self):
        return self.T_fecha
    def agregamedipago(self):
        return self.mediopago
    
class estudiante:
    def __init__ (self,Esco_curso,Actualizar):
        self.Esco_curso=Esco_curso
        self.Actualizar=Actualizar

    def admit(self):
        return self.Esco_curso
    
class register:
    def __init__ (self,id,nombre,edad,num_conta,nom_usu,contraseña):
        self.id=id
        self.nombre=nombre
        self.edad=edad
        self.num_conta=num_conta
        self.nom_usu=nom_usu
        self.contraseña=contraseña

    
    def agrid(self):
        return self.id
    def agrnombre(self):
        return self.nombre
    def agredad(self):
        return self.edad
    def agrnum_tel(self):
        return self.num_conta   
    def agrnom_usu(self):
        return self.nom_usu
    def agrclave(self):
        return self.contraseña
    
class instructor(register):
    def __init__(self,Usu_nom,Cla_instructor):
        self.Usu_nom=Usu_nom
        self.Cla_istructor=Cla_instructor

    def getN_inst(self):
        return self.Usu_nom
    
    def getC_inst(self):
        return self.Cla_istructor

class transaciones:
    def __init__ (self,T_ident,T_Detalles,T_fecha,mediopago):
        self.T_ident=T_ident
        self.T_Detalles=T_Detalles
        self.T_fecha=T_fecha
        self.mediopago=mediopago
    def agregaID(self):
        return self.T_ident
    def agregaDET(self):
        return self.T_Detalles
    def agregafecha(self):
        return self.T_fecha
    def agregamedipago(self):
        return self.mediopago
    
class estudiante:
    def __init__ (self,Esco_curso,Actualizar):
        self.Esco_curso=Esco_curso
        self.Actualizar=Actualizar

    def admit(self):
        return self.Esco_curso
    
    def update(self):
        return self.Actualizar
    
class materias:
    def __init__ (self,IDmateria,Nom_materia,Desc_materia,INS_asig,Hora_materia):
        self.IDmateria=IDmateria
        self.Nom_materia=Nom_materia
        self.Desc_materia=Desc_materia
        self.INS_asig=INS_asig
        self.Hora_materia=Hora_materia

    def sethoramateria(self):
        return self.Hora_materia
    
class curso:
    def __init__ (self,IDcurso,Desc_ambiente,Fecha_curso,Nivel_año):
        self.IDcurso=IDcurso
        self.Desc_ambiente=Desc_ambiente
        self.Fecha_curso=Fecha_curso
        self.Nivel_año=Nivel_año

    def setID(self):
        return self.IDcurso
    def setambiente(self):
        return self.Desc_ambiente
    def setfech(self):
        return self.Fecha_curso
    def setnivel(self):
        return self.Nivel_año
    
class inscripcion:
    def __init__ (self,idincrip,detallesincrip,reque,fechainscrip):
        self.idinscrip=idincrip
        self.detallesinscrip=detallesincrip
        self.reque=reque
        self.fechainscrip=fechainscrip

    def setID(self):
        return self.idinscrip
    def setdeta_inscri(self):
        return self.detallesinscrip
    def setRQ(self):
        return self.reque
    def setFEC(self):
        return self.fechainscrip
    

re=register('1007746634 ','Cesar Pulgarin ','23 ','3122744822 ','kaputbutton@gmail.com ','117')
it=instructor('javier','1234')
tr=transaciones('K-1894','CUPO','12/4/2023','Efectivo')
es=estudiante('Curso 234','Curso 117')
mt=materias('112','PROGRMAMCION','ORIENTADO A OBJETOS','Samuel Padilla','10:00 am')
cs=curso('234','Salon de Programacion','Empieza el dia 18/4/2023','Ninguno')
io=inscripcion('ID 198456','Aprender','Estar registrado','16/4/2023')


print('Cual es tu rol? \n 1 --> Instructor \n 2 --> Nuevo')
k=input('--> ')


while True:
    match k:
        case '1':
            l=str(input('ingrese su usuario: '))  
            j=int(input('ingrese su Contraseña: '))
            if l  == it.getN_inst():
                if j == int(it.getC_inst()): # casting convertir str en int
                    print('BIENVENIDO INSTRUCTOR',it.getN_inst())
                else:
                    print('error vuelva a ingresar sus credenciales XD')    
                print('MENU \n 1. registrar \n 2. Transaciones \n 3. Agregar materias' )
                ll=input(': ')
                if ll == '1': # una condicional, si el numero ingresado por teclado es igual a 1(registro)
                        ñ=input('ingresed su identificacion: ') # pasa a ingresar los datos de registro para el nuevo usuario 
                        it.agrid=ñ # decimos que variable es igual a la clase instructor,como hereda de la clase registro entonces el instructor podra hacer el registro.
                        a=input('ingresed su nombre y apellido: ')
                        it.agrnombre=a
                        b=input('ingresed su edad: ')
                        it.agredad=b
                        c=input('ingresed un telefono: ')
                        it.agrnum_tel=c
                        d=input('ingresed un nombre de usuario: ')
                        it.agrnom_usu=d
                        e=input('ingresed una Contraseña: ')
                        it.agrclave=e
                        print('ID: '+ it.agrid() +'\n Nombre y Apellido: '+ it.agrnombre() +'\n Edad: '+ it.agredad() +'\n Numero telefonico: '+ it.agrnum_tel() +'\n NOmbre Usuario: '+it.agrnom_usu() + '\n Clave: '+ it.agrclave())
                elif ll == '2':
                        print('Comprobante de cupo terminada'+'\n ID: ' +tr.agregaID() + '\n Detalles: '+tr.agregaDET()+'\n Fecha: '+ tr.agregafecha() + '\n Manera de pago: '+ tr.agregamedipago())
        case '2':
            ñ=input('ingresed su identificacion: ')
            ñ=re.agrid
            a=input('ingresed su nombre y apellido: ')
            a=re.agrnombre
            b=input('ingresed su edad: ')
            b=re.agredad
            c=input('ingresed un telefono: ')
            c=re.agrnum_tel
            d=input('ingresed un nombre de usuario: ')
            d=re.agrnom_usu
            e=input('ingresed una Contraseña: ')
            e=re.agrclave
            print('\n ID: '+re.agrid() +'\n Nombre y Apellido: '+ re.agrnombre() +'\n Edad: '+ re.agredad() +'\n Numero telefonico: '+ re.agrnum_tel() +'\n NOmbre Usuario: '+re.agrnom_usu() + '\n Clave: '+ re.agrclave())
            break




            






    
