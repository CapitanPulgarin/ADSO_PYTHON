def promedio(nota):
    if nota<0:
        print("Ingreso un rango de nota no equivalente")
    elif nota<=2:
        print("Insuficiente")
    elif nota>2 and nota<=4:
        print("suficiente")
    elif nota>4 and nota<=6:
        print("Bien")
    elif nota>6 and nota<=8:
        print("Eficiente")
    elif nota>8 and nota<=10:
        print("Excelente")
    else:
        print("Ingreso un rango de nota no equivalente")


nota = int(input("Escriba la nota del 0 al 10\n"))

promedio(nota)