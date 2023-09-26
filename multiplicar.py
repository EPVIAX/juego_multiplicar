import random

def juego(tabla_x, resp, aleatorios):
    """
    - tabla_x: el numero de la tabla de multiplicar que se desea practicar
    - resp: la cantidad de respuestas correctas que se tiene al momento
    - aleatorios: array de numeros enteros aleatorios del 1 al 10 sin repetición
    """

    correctas = resp
    texto = str('Ingrese la respuesta de: '+ str(tabla_x) + ' x '+ str(aleatorios[correctas]) + ' = ')
    respuesta = int(input(texto))
    if respuesta == tabla_x*aleatorios[correctas]:
        print("correcto es", respuesta, '\n')
        correctas += 1
        print(' Vas ', correctas, ' respuestas correctas\n')
        if correctas == 10:
            print('Excelente tienes ', correctas, 'respuestas correctas' )
            return
        else:
            juego(tabla_x, correctas, aleatorios)
    else:
        print("sigue practicando la respuesta es: ", tabla_x*aleatorios[correctas], '\n')
        correctas = 0
        print('Reiniciando ... tienes ', correctas, 'respuestas correctas\n' )
        aleatorios = random.sample(range(1, 11),10) #Generación de números aleatorios    
        juego(tabla_x, correctas, aleatorios)

""" --- Inicio del programa --- """
print ("   ")
print("*** Bienvenido al juego de las tablas de Multiplicar ***", '\n\n')
tabla_x = int(input('Ingresa el numero de la tabla que quieres practicar: '))
print('\n ----> practiquemos la tabla del ', tabla_x ,'... \n')
correctas = 0
aleatorios = random.sample(range(1, 11),10) #Generación de números aleatorios    
juego(tabla_x, correctas, aleatorios)

seguir = str(input('quieres seguir jugando? s=si n=no --> :'))
if seguir == "s":
    print ("   ")
    print("*** Bienvenido al juego de las tablas de Multiplicar ***", '\n\n')
    tabla_x = int(input('Ingresa el numero de la tabla que quieres practicar: '))
    print('\n ----> practiquemos la tabla del ', tabla_x ,'... \n')
    correctas = 0
    aleatorios = random.sample(range(1, 11),10) #Generación de números aleatorios    
    juego(tabla_x, correctas, aleatorios)
else:
    print('\n ... Fin del juego ...\n')