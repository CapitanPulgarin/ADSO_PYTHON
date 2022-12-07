import random
def calcularmaxmin(lista):
    return (max(lista)),(min(lista))


numeros=[]
for x in range(10):
    numeros.append(random.randint(1,100))

vmax,vmin=calcularmaxmin(numeros)
print('el valor maximo de', vmax)
print('el valor minimo de', vmin)