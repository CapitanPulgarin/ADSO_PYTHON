#not
def par_impar(indice,lista):
    sumapar=0
    sumaimpar=0
    if indice % 2 == 0:
        sumapar += lista[indice]
    else:
        sumaimpar += lista[indice]
    return sumapar

def par_impar2(indice,lista):
    sumapar=0
    sumaimpar=0
    if indice % 2 == 0:
        sumapar += lista[indice]
    else:
        sumaimpar += lista[indice]
        promedioimpar = sumaimpar//len(lista)
    return promedioimpar


import random

tam=random.randint(10,25)
lista=[]

for indice in range(tam):
    lista.append(round(random.random()*100))
    par_impar(indice,lista)
print(lista,"\nLa lista tiene un tamaño de: ", len(lista))
print('La suma de los pares es de:',par_impar(indice,lista),'\nY el promedio de los impares es de:',par_impar2(indice,lista))