def listaPrimos(lista):
    primos = []
    for i in range(len(lista)):
        divisores = 0
        for j in range(1,101):
            if lista[i] % j == 0:
                divisores += 1
        if divisores == 2:
            primos.append(lista[i])
    print("Hay",len(primos),"números primos","\nSon los siguientes: ",primos)


import random

tam=random.randint(10,25)
lista=[]

for indice in range(tam):
    lista.insert(indice,round(random.random()*100))
print(lista,"\nLa lista tiene un tamaño de: ", len(lista))

listaPrimos(lista)