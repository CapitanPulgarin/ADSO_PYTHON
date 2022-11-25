def igualPromedio(lista,promedio):
    for indice in range(len(lista)):
        if lista[indice] == promedio:
            print("El valor ",lista[indice],"es igual al promedio ",promedio)
        elif lista[indice] > promedio:
            print("El valor ",lista[indice],"es mayor al promedio ",promedio)
        elif lista[indice] < promedio:
            print("El valor ",lista[indice],"es menor al promedio ",promedio)

import random

tam=random.randint(10,25)
lista=[]

for indice in range(tam):
    lista.append(round(random.random()*100))
print(lista,"\nLa lista tiene un tamaño de: ", len(lista))

suma=0

for indice in range(len(lista)):
    suma += lista[indice]
promedio = suma//len(lista)

print('El promedio es: ',promedio)

igualPromedio(lista,promedio)
