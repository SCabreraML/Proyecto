def crear_sistema():
    """
    Crea un sistema de ecuaciones ingresado por el usuario.
    
    Retorna:
        list: Una lista de listas que representa el sistema de ecuaciones.
              Cada sublista contiene los coeficientes de las variables y el término independiente.
    """
    print("Ingrese el sistema de ecuaciones")
    num_ecuaciones = int(input("Ingrese el número de ecuaciones: "))
    num_variables = int(input("Ingrese el número de variables: "))
    
    sistema = []
    for i in range(num_ecuaciones):
        ecuacion = []
        print(f"\nIngrese los coeficientes de la ecuación {i + 1}:")
        for j in range(num_variables):
            coeficiente = float(input(f"Coeficiente de x{j + 1}: "))
            ecuacion.append(coeficiente)
        termino_independiente = float(input("Ingrese el término independiente: "))
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
    """
    Calcula el determinante de una matriz cuadrada.
    
    Parámetros:
        matriz (list): Una lista de listas que representa una matriz cuadrada.
    
    Retorna:
        float: El determinante de la matriz.
    """
    n = len(matriz)
    if n == 1:
        return matriz[0][0]
    elif n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    elif n == 3:
        # Regla de Sarrus para matrices 3x3
        det = (
            matriz[0][0] * matriz[1][1] * matriz[2][2]
            + matriz[0][1] * matriz[1][2] * matriz[2][0]
            + matriz[0][2] * matriz[1][0] * matriz[2][1]
            - matriz[0][2] * matriz[1][1] * matriz[2][0]
            - matriz[0][0] * matriz[1][2] * matriz[2][1]
            - matriz[0][1] * matriz[1][0] * matriz[2][2]
        )
        return det
    else:
        raise ValueError("El método de álgebra matricial solo es válido para sistemas 2x2 o 3x3.")


def obtener_matriz_inversa(matriz):
    """
    Calcula la matriz inversa de una matriz cuadrada.
    
    Parámetros:
        matriz (list): Una lista de listas que representa una matriz cuadrada.
    
    Retorna:
        list: La matriz inversa.
    """
    n = len(matriz)
    det = calcular_determinante(matriz)
    
    if det == 0:
        raise ValueError("La matriz no tiene inversa (determinante = 0).")
    
    if n == 2:
        # Matriz inversa para 2x2
        a, b = matriz[0][0], matriz[0][1]
        c, d = matriz[1][0], matriz[1][1]
        inversa = [
            [d / det, -b / det],
            [-c / det, a / det]
        ]
    elif n == 3:
        # Matriz inversa para 3x3
        # Calculamos la matriz de cofactores
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
        
        # Matriz adjunta (transpuesta de la matriz de cofactores)
        adjunta = list(map(list, zip(*cofactores)))
        
        # Matriz inversa: adjunta dividida por el determinante
        inversa = [[adjunta[i][j] / det for j in range(n)] for i in range(n)]
    else:
        raise ValueError("El método de álgebra matricial solo es válido para sistemas 2x2 o 3x3.")
    
    return inversa


def resolver_por_algebra_matricial(sistema):
    """
    Resuelve un sistema de ecuaciones lineales utilizando el método de álgebra matricial.
    
    Parámetros:
        sistema (list): Una lista de listas que representa el sistema de ecuaciones.
    
    Retorna:
        list: Una lista con las soluciones del sistema (valores de las variables).
              Retorna None si el sistema no tiene solución única.
    """
    # Extraer la matriz de coeficientes y el vector de términos independientes
    coeficientes = [ecuacion[:-1] for ecuacion in sistema]  # Excluir el término independiente
    terminos_independientes = [ecuacion[-1] for ecuacion in sistema]  # Solo el término independiente
    
    print("\nPaso 1: Escribir el sistema en forma matricial AX = B")
    print("Matriz de coeficientes (A):")
    for fila in coeficientes:
        print(fila)
    print("Vector de términos independientes (B):")
    print(terminos_independientes)
    
    # Obtener la matriz inversa de los coeficientes
    try:
        print("\nPaso 2: Calcular la inversa de la matriz A (A⁻¹)")
        inversa = obtener_matriz_inversa(coeficientes)
        print("Matriz inversa (A⁻¹):")
        for fila in inversa:
            print(fila)
    except ValueError as e:
        print(e)
        return None
    
    # Multiplicar la matriz inversa por el vector de términos independientes
    print("\nPaso 3: Multiplicar A⁻¹ por B para obtener X")
    soluciones = []
    n = len(inversa)
    for i in range(n):
        solucion = sum(inversa[i][j] * terminos_independientes[j] for j in range(n))
        soluciones.append(solucion)
    
    print("Vector de soluciones (X):")
    print(soluciones)
    
    return soluciones


def resolver_por_crammer(sistema):
    """
    Resuelve un sistema de ecuaciones lineales utilizando el método de Cramer.
    
    Parámetros:
        sistema (list): Una lista de listas que representa el sistema de ecuaciones.
    
    Retorna:
        list: Una lista con las soluciones del sistema (valores de las variables).
              Retorna None si el sistema no tiene solución única.
    """
    # Extraer la matriz de coeficientes y el vector de términos independientes
    coeficientes = [ecuacion[:-1] for ecuacion in sistema]  # Excluir el término independiente
    terminos_independientes = [ecuacion[-1] for ecuacion in sistema]  # Solo el término independiente
    
    print("\nPaso 1: Escribir el sistema en forma matricial AX = B")
    print("Matriz de coeficientes (A):")
    for fila in coeficientes:
        print(fila)
    print("Vector de términos independientes (B):")
    print(terminos_independientes)
    
    # Calcular el determinante de la matriz de coeficientes
    print("\nPaso 2: Calcular el determinante de A (det(A))")
    det_A = calcular_determinante(coeficientes)
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
            print(fila)
        det_temp = calcular_determinante(matriz_temp)
        print(f"det(A{i + 1}) = {det_temp}")
        
        # Calcular la solución para la variable i
        solucion = det_temp / det_A
        soluciones.append(solucion)
        print(f"x{i + 1} = det(A{i + 1}) / det(A) = {solucion:.2f}")
    
    return soluciones


def resolver_por_gauss_jordan(sistema):
    """
    Resuelve un sistema de ecuaciones lineales utilizando el método de Gauss-Jordan.
    
    Parámetros:
        sistema (list): Una lista de listas que representa el sistema de ecuaciones.
    
    Retorna:
        list: Una lista con las soluciones del sistema (valores de las variables).
              Retorna None si el sistema no tiene solución única.
    """
    n = len(sistema)
    
    # Crear la matriz aumentada
    matriz_aumentada = [fila.copy() for fila in sistema]
    
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


# Menú principal
categoria = 0
sistema = []  # Variable para almacenar el sistema de ecuaciones

while categoria != 5:
    print("\n1. Crear sistema de ecuaciones")
    print("2. Resolver por método de Crammer")
    print("3. Resolver por el método de algebra matricial")
    print("4. Resolver por el método de Gauss-Jordan")
    print("5. Salir")
    categoria = int(input("Ingresa la opción: "))
    
    match categoria:
        case 1:
            sistema = crear_sistema()  # Llamada a la función para crear el sistema
        
        case 2:
            if sistema:  # Verifica si el sistema ha sido creado
                print("\nResolviendo por el método de Crammer...")
                soluciones = resolver_por_crammer(sistema)
                if soluciones:
                    print("\nSoluciones encontradas:")
                    for i, solucion in enumerate(soluciones):
                        print(f"x{i + 1} = {solucion:.2f}")
            else:
                print("Primero debes crear un sistema de ecuaciones.")
        
        case 3:
            if sistema:  # Verifica si el sistema ha sido creado
                print("\nResolviendo por el método de álgebra matricial...")
                soluciones = resolver_por_algebra_matricial(sistema)
                if soluciones:
                    print("\nSoluciones encontradas:")
                    for i, solucion in enumerate(soluciones):
                        print(f"x{i + 1} = {solucion:.2f}")
            else:
                print("Primero debes crear un sistema de ecuaciones.")
        
        case 4:
            if sistema:  # Verifica si el sistema ha sido creado
                print("\nResolviendo por el método de Gauss-Jordan...")
                soluciones = resolver_por_gauss_jordan(sistema)
                if soluciones:
                    print("\nSoluciones encontradas:")
                    for i, solucion in enumerate(soluciones):
                        print(f"x{i + 1} = {solucion:.2f}")
            else:
                print("Primero debes crear un sistema de ecuaciones.")
        
        case 5:
            print("Saliendo del programa...")
        
        case _:
            print("Opción no válida. Intente de nuevo.")