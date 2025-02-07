from matplotlib import pyplot as plt
import numpy as np


### FUNCIONES DE SISTEMAS DE ECUACIONES 3x3

def crear_sistema():
    print("Ingrese el sistema de ecuaciones 3x3")
    
    sistema = []
    for i in range(3):
        ecuacion = []
        print(f"\nIngrese los coeficientes de la ecuación {i + 1}:")
        for j in range(3):
            while True:
                try:
                    coeficiente = float(input(f"Coeficiente de x{j + 1}: "))
                    break
                except ValueError:
                    print("Error: Ingrese un número válido.")
            ecuacion.append(coeficiente)
        while True:
            try:
                termino_independiente = float(input("Ingrese el término independiente: "))
                break
            except ValueError:
                print("Error: Ingrese un número válido.")
        ecuacion.append(termino_independiente)
        sistema.append(ecuacion)
    
    print("\nSistema de ecuaciones ingresado:")
    for ecuacion in sistema:
        ecuacion_str = ""
        for j in range(len(ecuacion) - 1):  
            coeficiente = ecuacion[j]
            variable = f"x{j + 1}"
            if coeficiente >= 0 and j != 0:  
                ecuacion_str += f" + {coeficiente}{variable}"
            else:
                ecuacion_str += f" {coeficiente}{variable}"
        ecuacion_str += f" = {ecuacion[-1]}"  
        print(ecuacion_str)
    
    return sistema



def calcular_determinante(matriz):
    n = len(matriz)
    if n == 3:
        # REGLA DE SARRUS
        det = (
            matriz[0][0] * matriz[1][1] * matriz[2][2]
            + matriz[0][1] * matriz[1][2] * matriz[2][0]
            + matriz[0][2] * matriz[1][0] * matriz[2][1]
            - matriz[0][2] * matriz[1][1] * matriz[2][0]
            - matriz[0][0] * matriz[1][2] * matriz[2][1]
            - matriz[0][1] * matriz[1][0] * matriz[2][2]
        )
        return det




def obtener_matriz_inversa(matriz):
    n = len(matriz)
    det = calcular_determinante(matriz)

    if det is None:
        return None
    
    if det == 0:
        print("Error: La matriz no tiene inversa (determinante = 0).")
        return None
        
    elif n == 3:
        # Matriz inversa para 3x3
        cofactores = []
        for i in range(n):
            fila_cofactores = []
            for j in range(n):
                # Matriz menor (eliminamos la fila i y la columna j)
                menor = [fila[:j] + fila[j + 1:] for fila in (matriz[:i] + matriz[i + 1:])]
                # Cofactor: (-1)^(i+j) * determinante del menor
                cofactor = ((-1) ** (i + j)) * calcular_determinante(menor)
                fila_cofactores.append(cofactor)
            cofactores.append(fila_cofactores)
        
        # Calcular la matriz adjunta (transpuesta de la matriz de cofactores)
        adjunta = []
        for j in range(n):  # Iterar sobre columnas
            fila_adjunta = []
            for i in range(n):  # Iterar sobre filas
                fila_adjunta.append(cofactores[i][j])  # Transponer: intercambiar filas y columnas
            adjunta.append(fila_adjunta)
        
        # Matriz inversa: adjunta dividida por el determinante
        inversa = [[adjunta[i][j] / det for j in range(n)] for i in range(n)]
    else:
        print("Error: El método de álgebra matricial solo es válido para sistemas 2x2 o 3x3.")
        return None
    
    return inversa



def resolver_por_algebra_matricial(sistema):
    # EXTRAER MATRIZ X (COEFICIENTES) Y VECTOR DE TERMINOS INDEPENDIENTES
    coeficientes = [ecuacion[:-1] for ecuacion in sistema]  # Excluir el término independiente
    terminos_independientes = [ecuacion[-1] for ecuacion in sistema]  # Solo el término independiente
    
    print("\nPaso 1: Escribir el sistema en forma matricial AX = B")
    print("Matriz de coeficientes (A):")
    for fila in coeficientes:
        print(fila)
    print("Vector de términos independientes (B):")
    print(terminos_independientes)
    
    # Obtener la matriz inversa de los coeficientes
    print("\nPaso 2: Calcular la inversa de la matriz A (A⁻¹)")
    inversa = obtener_matriz_inversa(coeficientes)
    if inversa is None:
        return None
    
    print("Matriz inversa (A⁻¹):")
    for fila in inversa:
        print(fila)
    
    # Multiplicar la matriz inversa por el vector de términos independientes
    print("\nPaso 3: Multiplicar A⁻¹ por B para obtener X")
    soluciones = []
    n = len(inversa)
    for i in range(n):
        solucion = 0  # Inicializar la suma
        for j in range(n):
            solucion += inversa[i][j] * terminos_independientes[j]  # Sumar manualmente
        soluciones.append(solucion)
    
    print("Vector de soluciones (X):")
    print(soluciones)
    
    return soluciones


def resolver_por_crammer(sistema):
    # Extraer la matriz de coeficientes y el vector de términos independientes
    coeficientes = [ecuacion[:-1] for ecuacion in sistema]  # Excluir el término independiente
    terminos_independientes = [ecuacion[-1] for ecuacion in sistema]  # Solo el término independiente
    
    print("\nPaso 1: Escribir el sistema en forma matricial AX = B")
    print("\nMatriz de coeficientes (A):")
    for fila in coeficientes:
        print(fila)
    print("Vector de términos independientes (B):")
    print(terminos_independientes)
    
    # Calcular el determinante de la matriz de coeficientes
    print("\nPaso 2: Calcular el determinante de A (det(A))")
    det_A = calcular_determinante(coeficientes)
    if det_A is None:
        return None
    
    print(f"det(A) = {det_A}")
    
    if det_A == 0:
        print("El sistema no tiene solución única (determinante = 0).")
        return None
    
    n = len(coeficientes)
    soluciones = []
    
    # Calcular las soluciones utilizando la regla de Cramer
    print("\nPaso 3: Calcular los determinantes para cada variable")
    for i in range(n):
        # Crear una copia de la matriz de coeficientes
        matriz_temp = [fila.copy() for fila in coeficientes]
        
        # Reemplazar la columna i con el vector de términos independientes
        for j in range(n):
            matriz_temp[j][i] = terminos_independientes[j]
        
        # Calcular el determinante de la matriz modificada
        print(f"Matriz modificada para x{i + 1}:")
        for fila in matriz_temp:
            print(f"\n{fila}")
        det_temp = calcular_determinante(matriz_temp)
        if det_temp is None:
            return None
        
        print(f"det(A{i + 1}) = {det_temp}")
        
        # Calcular la solución para la variable i
        solucion = det_temp / det_A
        soluciones.append(solucion)
        print(f"x{i + 1} = det(A{i + 1}) / det(A) = {solucion:.2f}")
    
    return soluciones



def resolver_por_gauss_jordan(sistema):
    n = len(sistema)
    
    # Crear la matriz aumentada
    matriz_aumentada = []
    for fila in sistema:
        nueva_fila = []  
        for elemento in fila:
            nueva_fila.append(elemento)  # Copiar cada elemento de la fila
        matriz_aumentada.append(nueva_fila)  # Agregar la nueva fila a la matriz aumentada
    
    print("\nPaso 1: Escribir el sistema en forma de matriz aumentada [A | B]")
    print("Matriz aumentada:")
    for fila in matriz_aumentada:
        print(fila)
    
    # Aplicar el método de Gauss-Jordan
    print("\nPaso 2: Aplicar operaciones elementales de fila para obtener la forma RREF")
    for i in range(n):
        # Hacer que el elemento diagonal sea 1
        if matriz_aumentada[i][i] == 0:
            # Buscar una fila para intercambiar
            for j in range(i + 1, n):
                if matriz_aumentada[j][i] != 0:
                    matriz_aumentada[i], matriz_aumentada[j] = matriz_aumentada[j], matriz_aumentada[i]
                    print(f"\nIntercambiar fila {i + 1} con fila {j + 1}:")
                    for fila in matriz_aumentada:
                        print(fila)
                    break
            else:
                print("El sistema no tiene solución única.")
                return None
        
        # Dividir la fila i por el elemento diagonal
        divisor = matriz_aumentada[i][i]
        for j in range(i, n + 1):
            matriz_aumentada[i][j] /= divisor
        print(f"\nDividir fila {i + 1} por {divisor}:")
        for fila in matriz_aumentada:
            print(fila)
        
        # Hacer ceros en las otras filas
        for k in range(n):
            if k != i:
                factor = matriz_aumentada[k][i]
                for j in range(i, n + 1):
                    matriz_aumentada[k][j] -= factor * matriz_aumentada[i][j]
                print(f"\nRestar {factor} veces la fila {i + 1} a la fila {k + 1}:")
                for fila in matriz_aumentada:
                    print(fila)
    
    # Extraer las soluciones
    soluciones = [matriz_aumentada[i][n] for i in range(n)]
    
    print("\nPaso 3: Leer las soluciones directamente de la matriz RREF")
    print("Soluciones:")
    for i, solucion in enumerate(soluciones):
        print(f"x{i + 1} = {solucion:.2f}")
    
    return soluciones

### CÓDIGO

opcion = 0
while opcion != 3:
    try:
        print("\n1. Modelar funciones matemáticas")
        print("2. Resolver sistemas de ecuaciones")
        print("3. Salir")
        opcion = int(input("Ingrese la opción a realizar: "))

        match opcion:
            case 1:
                print("Modelar funciones")
            case 2:
                categoria = 0
                while categoria != 5:
                    print("\n1. Crear sistema de ecuaciones")
                    print("2. Resolver por método de Crammer")
                    print("3. Resolver por el método de álgebra matricial")
                    print("4. Resolver por el método de Gauss-Jordan")
                    print("5. Salir")
                    categoria = int(input("Ingresa la opción: "))
                    
                    match categoria:
                        case 1:
                            sistema = crear_sistema()
                        case 2:
                            if sistema:
                                soluciones = resolver_por_crammer(sistema)
                            else:
                                print("Primero debes crear un sistema de ecuaciones.")
                        case 3:
                            if sistema:
                                soluciones = resolver_por_algebra_matricial(sistema)
                            else:
                                print("Primero debes crear un sistema de ecuaciones.")
                        case 4:
                            if sistema:
                                soluciones = resolver_por_gauss_jordan(sistema)
                            else:
                                print("Primero debes crear un sistema de ecuaciones.")
                        case 5:
                            print("Saliendo del programa...")
                        case _:
                            print("Opción no válida. Intente de nuevo.")
            case 3:
                print("\nPrograma terminado, Adiós!")
            case _:
                print("Opción no válida. Intente de nuevo.")

    except ValueError:
        print("\nError: Ingrese un número válido.")
    except ZeroDivisionError:
        print("\nError: No se puede dividir entre 0.")
    except Exception as e:
        print(f"\nHa ocurrido un error inesperado: {e}")
