def l_suma(lista):
    suma=0
    for indice in range(len(lista)):
        suma += lista[indice]
    return suma 


def l_promedio(lista):
    suma=0
    for indice in range(len(lista)):
        suma += lista[indice]
    promedio = suma//len(lista)
    return promedio

import random

lista=[int(random.random()*100) for i in range (random.randint(10,25))]
print(lista,"\nLa lista tiene un tamaño de: ", len(lista))

print('La suma es de la lista es:',l_suma(lista),'Y el promedio es: ',l_promedio(lista))

