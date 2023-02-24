def conespacio(cad):
    parconespacio=cad.replace('',' ')
    parconespacio.strip()
    return parconespacio

mensaje= input('escribe una palabra: ')
print('la palabra con espacio:',conespacio(mensaje))