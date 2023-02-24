def calculartem(temp1,temp2):
    return (temp1 + temp2)/2

cant=int(input('cuantas temperatura quiere calcular?'))
for x in range(cant):
    tmax = float(input('intrduzca una temperatura maxima:'))
    tmin= float(input('intrduzca una temperatura maxima'))
    print('temperatura media:'calculartem(tmax,tmin))