from matplotlib import pyplot as plt
import numpy as np

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

    except Exception as e:
        print(f"Error al graficar la función: {e}")

# Llamar a la función
graficar_funciones()