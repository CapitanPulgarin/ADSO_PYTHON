def igualdad(num1,num2,num3):
    if num1 == num2 and num1 == num3:
        print("los números son iguales")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print ("Hay 2 numeros iguales")
    else:
        print ("todos los números son diferentes")

num1 = int(input("Escriba primer número\n"))
num2 = int(input("Escriba segundo número\n"))
num3 = int(input("Escriba tercer número\n"))

igualdad(num1,num2,num3)
