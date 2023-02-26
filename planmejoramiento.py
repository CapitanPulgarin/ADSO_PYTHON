'''#listas con bucle
import random

temp=[]
for i in range(30):
    temp.append(round(random.randint(4,30)))
    print(i)
print(temp)

list=[]
for x in range(20):
    list.append(round(random.randint(5,20)))
    print('tiene',x,'años')
print(list)

list2=[]
for w in range(40):
    list2.append(round(random.randint(2,8)))
    print('sofia tienes',w,'hermanos')
print(list2)

#lista con rebanadas

vec=[1,2,3,4,5,6]
vec2=vec[1:-3]
print(vec2)

ra=['jose','brayan','justin','maria','camila','daniela']
k=ra[2:-3]
print(k)

jo=['mouse',34,'eagle',98,'pig',678]
ja=jo[1:-3]
print(ja)

mor=[34,56,7,89,4,2,14,567,8]
print(mor[2:])

cap=[87,908,564,90,0,45,34,6798,900,987,564,1]
print(cap[4:])

jor=[67,90,0,671,45,100,768,65,34,232,2]
print(jor[:-7])

kort=['maria','jhon','karen','lucas']
print(kort[:])

ñandu=['kakarotto','krillin','vegeta','picoro']
print(ñandu[:])

o=['cortana','jhon','Dr halsey','inquisidor','the flood']
print(o[:])

#bucle for

for i in range(10,-1,-2):
    print(i)

for h in range(-20,1,2):
    print(h)

for g in range(40,-1,-3):
    print(g)

#funciones con bucle listas

def mi_funcion(listas):
    lista2=[]
    for h in list3:
        if h in lista2:
            lista2.append(h)
    print(lista2)

list3=[34,56,7,89,54,3,4,56,7,87,9]
mi_funcion(list3)'''

def k(o):
    ces=[]
    for v in y:
        if v not in ces:
            ces.append(v)
    print(ces)

y=['cesar','arnedys','pulgarin','herron']
k(y)