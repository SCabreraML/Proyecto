from matplotlib import pyplot as plt
import numpy as np

def graficar_funcion():
    try:
        
        expresion = input("Ingrese la función en términos de x (ejemplo: x**2 + 2*x - 3): ")

        
        x = np.linspace(-10, 10, 400)  

        # Evaluar la función usando eval()
        y = [eval(expresion, {"x": val, "np": np}) for val in x]

        
        plt.figure(figsize=(8, 5))
        plt.plot(x, y, label=f"f(x) = {expresion}", color="blue")
        plt.axhline(0, color='black', linewidth=0.5)  # Eje X
        plt.axvline(0, color='black', linewidth=0.5)  # Eje Y
        plt.grid(True, linestyle="--", linewidth=0.5)
        plt.legend()
        plt.title("Gráfico de la función")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.show()
    
    except Exception as e:
        print(f"Error al graficar la función: {e}")

graficar_funcion()