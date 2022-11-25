def primo(num): 
    cont=0
    for i in  range(2,num+1):
        if num % i == 0:
            cont+=1
    if cont >2:
        print('no primo')
    else:
        print('es primo')    

num=int(input('ingresar un numero: '))
primo(num)