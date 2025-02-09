from matplotlib import pyplot as plt
import numpy as np

### FUNCIONES MATEMÀTICAS


def graficar_funciones():
    try:
        while True:
            num_funciones = int(input("¿Cuántas funciones deseas graficar? (mínimo 1, máximo 3): "))
            
            if num_funciones < 1 or num_funciones > 3:
                print("Debes ingresar un número entre 1 y 3.")
            else:
                break
                return
        
        funciones = []  # Lista para almacenar las expresiones ingresadas

        for i in range(num_funciones):
            expresion = input(f"Ingrese la función {i+1} en términos de x (ejemplo: x**2 + 2*x - 3): ")
            funciones.append(expresion)

        x = np.linspace(-10, 10, 400)  # Rango de valores para x
        
        # Crear una figura con 3 subgráficos en una columna
        fig, axes = plt.subplots(3, 1, figsize=(8, 12))  # 3 filas, 1 columna

        # Dibujar cada función en un subgráfico diferente
        colores = ['blue', 'red', 'green']  # Colores para cada gráfica
        
        for i in range(num_funciones):
            y = [eval(funciones[i], {"x": val, "np": np}) for val in x]
            axes[i].plot(x, y, color=colores[i], label=f"f(x) = {funciones[i]}")
            axes[i].axhline(0, color='black', linewidth=0.5)  # Eje X
            axes[i].axvline(0, color='black', linewidth=0.5)  # Eje Y
            axes[i].grid(True, linestyle="--", linewidth=0.5)
            axes[i].legend()
            axes[i].set_title(f"Gráfico {i+1}")
            axes[i].set_xlabel("x")
            axes[i].set_ylabel("f(x)")

        # Ajustar la disposición de los gráficos
        plt.tight_layout()
        plt.show()

    except ValueError:
        print("Error, ingrese un número")
    except Exception as e:
        print(f"Error al graficar la función: {e}")

### FUNCIONES ÁLGEBRA

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
    
    # CONVERSIÖN A CADENA DE TEXTO
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
    if n == 1:
        return matriz[0][0]
    elif n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    elif n == 3:
        # SARRUS
        det = (
            matriz[0][0] * matriz[1][1] * matriz[2][2]
            + matriz[0][1] * matriz[1][2] * matriz[2][0]
            + matriz[0][2] * matriz[1][0] * matriz[2][1]
            - matriz[0][2] * matriz[1][1] * matriz[2][0]
            - matriz[0][0] * matriz[1][2] * matriz[2][1]
            - matriz[0][1] * matriz[1][0] * matriz[2][2]
        )
        return det

def calcular_matriz_adjunta(matriz):
    n = len(matriz)
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
    
    # CALCULAR MATRIZ ADJUNTA
    adjunta = []
    for j in range(n):  
        fila_adjunta = []
        for i in range(n):  
            fila_adjunta.append(cofactores[i][j])  # TRASPONER: INTERCARMBIAR FILAS POR COLUMNAS
        adjunta.append(fila_adjunta)
    
    return adjunta

def obtener_matriz_inversa(matriz):
    n = len(matriz)
    det = calcular_determinante(matriz)
    
    if det is None:
        return None
    
    if det == 0:
        print("Error: La matriz no tiene inversa (determinante = 0).")
        return None
        
    elif n == 3:
        # INVERSA
        cofactores = []
        for i in range(n):
            fila_cofactores = []
            for j in range(n):
                menor = [fila[:j] + fila[j + 1:] for fila in (matriz[:i] + matriz[i + 1:])]
                cofactor = ((-1) ** (i + j)) * calcular_determinante(menor)
                fila_cofactores.append(cofactor)
            cofactores.append(fila_cofactores)
        
        # CALCULAR ADJUNTA
        adjunta = []
        for j in range(n): 
            fila_adjunta = []
            for i in range(n):  
                fila_adjunta.append(cofactores[i][j])  # TRASPONER
            adjunta.append(fila_adjunta)
        
        # Matriz inversa: adjunta dividida por el determinante
        inversa = [[adjunta[i][j] / det for j in range(n)] for i in range(n)]
    else:
        print("Error: El método de álgebra matricial solo es válido para sistemas 2x2 o 3x3.")
        return None
    
    return inversa



def resolver_por_algebra_matricial(sistema):
    # EXTRAER MATRIZ DE COEFICIENTES Y VECTOR DE TERMINOS INDEPENDIETES
    coeficientes = [ecuacion[:-1] for ecuacion in sistema]  # TERMINO INDEPENDIENTE
    terminos_independientes = [[ecuacion[-1]] for ecuacion in sistema]  # CONVERSIÖN DE MATRIZ FILA A MATRIZ COLUMNA
    
    print("\nPaso 1: Escribir el sistema en forma matricial AX = B")
    print("Matriz de coeficientes (A):")
    for fila in coeficientes:
        print(fila)
    print("\nVector de términos independientes (B):")
    for fila in terminos_independientes:
        print(fila)
    
    print("\nPaso 2: Calcular la matriz adjunta de A (Adj(A))")
    adjunta = calcular_matriz_adjunta(coeficientes)
    if adjunta is None:
        return None
    
    print("\nMatriz adjunta (Adj(A)):")
    for fila in adjunta:
        print(fila)
    
    print("\nPaso 3: Calcular la inversa de la matriz A (A⁻¹)")
    inversa = obtener_matriz_inversa(coeficientes)
    if inversa is None:
        return None
    
    print("\nMatriz inversa (A⁻¹):")
    for fila in inversa:
        print(fila)
    
    print("\nPaso 4: Multiplicar A⁻¹ por B para obtener X")
    soluciones = []
    n = len(inversa)
    for i in range(n):
        solucion = 0  
        for j in range(n):
            solucion += inversa[i][j] * terminos_independientes[j][0]  
        soluciones.append([solucion])  
    
    print("\nVector de soluciones (X):")
    for fila in soluciones:
        print(fila)
    
    return soluciones


def resolver_por_crammer(sistema):
    # EXTRAER MATRIZ DE COEFICIENTES Y VECTOR DE TERMINOS
    coeficientes = [ecuacion[:-1] for ecuacion in sistema]  # Excluir el término independiente
    terminos_independientes = [ecuacion[-1] for ecuacion in sistema]  # VECTOR
    
    print("\nPaso 1: Escribir el sistema en forma matricial AX = B")
    print("Matriz de coeficientes (A):")
    print("")
    for fila in coeficientes:
        print(fila)
    print("Vector de términos independientes (B):")
    print("")
    print(terminos_independientes)
    
    print("\nPaso 2: Calcular el determinante de A (det(A))")
    det_A = calcular_determinante(coeficientes)
    if det_A is None:
        return None
    
    print(f"\ndet(A) = {det_A}")
    
    if det_A == 0:
        print("El sistema no tiene solución única (determinante = 0).")
        return None
    
    n = len(coeficientes)
    soluciones = []
    
    print("\nPaso 3: Calcular los determinantes para cada variable")
    for i in range(n):
        matriz_temp = [fila.copy() for fila in coeficientes]
        for j in range(n):
            matriz_temp[j][i] = terminos_independientes[j]
        
        print(f"\nMatriz modificada para x{i + 1}:")
        print("")
        for fila in matriz_temp:
            print(fila)
        det_temp = calcular_determinante(matriz_temp)
        if det_temp is None:
            return None
        
        print(f"\ndet(A{i + 1}) = {det_temp}")
        
        solucion = det_temp / det_A
        soluciones.append(solucion)
        print(f"x{i + 1} = det(A{i + 1}) / det(A) = {solucion:.2f}")
    
    return soluciones



def resolver_por_gauss_jordan(sistema):
    n = len(sistema)
    matriz_aumentada = []
    for fila in sistema:
        nueva_fila = []  
        for elemento in fila:
            nueva_fila.append(elemento)  # COPIAR CADA ELEMENTO DE LA FILA
        matriz_aumentada.append(nueva_fila)  # AGREGA LA FILA A LA MATRIZ AUMENTADA
    
    print("\nPaso 1: Escribir el sistema en forma de matriz aumentada [A | B]")
    print("Matriz aumentada:")
    for fila in matriz_aumentada:
        print(fila)
    
    print("\nPaso 2: Aplicar operaciones elementales de fila para obtener la forma RREF")
    for i in range(n):
        # HACER ELEMENTO DIAGONAL SEA 1
        if matriz_aumentada[i][i] == 0:
            # BUSCA UNA FILA PARA INTERCAMBIAR
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
        
        # DIVIDIR FILA POR ELEMENTO DIAGONAL
        divisor = matriz_aumentada[i][i]
        for j in range(i, n + 1):
            matriz_aumentada[i][j] /= divisor
        print(f"\nDividir fila {i + 1} por {divisor}:")
        for fila in matriz_aumentada:
            print(fila)
        
        # HACER 0 EN LAS OTRAS FILAS
        for k in range(n):
            if k != i:
                factor = matriz_aumentada[k][i]
                for j in range(i, n + 1):
                    matriz_aumentada[k][j] -= factor * matriz_aumentada[i][j]
                print(f"\nRestar {factor} veces la fila {i + 1} a la fila {k + 1}:")
                for fila in matriz_aumentada:
                    print(fila)
    
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
        opcion = int(input("\nIngrese la opción a realizar: "))

        match opcion:
            case 1:
                graficar_funciones()
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
            case 3:
                print("\nEl programa ha terminado, Adiós!")
                print("")

    except ValueError:
        print("Error: Ingrese un número válido.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre 0.")
    except ImportError:
        print("Error: No se pudo importar matplotlib. Asegúrese de tenerlo instalado.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
