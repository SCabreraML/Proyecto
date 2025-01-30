from matplotlib import pyplot as plt
import numpy as np


def crear_matriz(filas, columnas):
    return [[int(input(f"Ingrese el valor en la posición {i},{j}: ")) for j in range(columnas)] for i in range(filas)]


def imprimir_matriz(matriz, nombre):
    if matriz is None:
        print(f"La matriz {nombre} no existe.")
    else:
        print(f"Matriz {nombre}:")
        for fila in matriz:
            print(fila)

def transponer_matriz(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]






try:
    opcion = 0
    while opcion!= 3:
        print("")
        print("1. Modelar funciones matemáticas")
        print("2. Resolver sistemas de ecuaciones")
        print("3. Salir")
        print("")
        opcion = int(input("Ingrese la opción a realizar:  "))



        match opcion:
            case 1:
                print("Modelar funciones")

            case 2:
                categoria=0
                while categoria!=4:
                     print("1. Crear sistema de ecuaciones")
                     print("2. Resolver por metodo de Crammer")
                     print("3. Resolver por el metodo de algebra matricial")
                     print("4. Resolver por el metodo de Gauss-Jordan")
                     categoria= int(input("Ingresa la opción: "))



                    



            case 3:
                print("Cierre de programa")
        


    

##Errores
except ValueError:
    print("Error al convertir")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except Exception as e:                      ## e es una variabe y contiene los errores  ## Exception es una excepcion generica de error
    print(f"Ha ocurrido un error inesperado {e}")       #Except son obligatorios
else:
    print("")                           ## Si es exitoso hace eso

finally:                                        ##No importa si es exitoso o no va a hacer algo
    print("")
    print("Programa terminado")
    print("")