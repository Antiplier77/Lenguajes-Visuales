import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

#Definir los valores de entrada
entry_pendiente_m = None
entry_intercepto_b = None

def graficar_recta():
    global entry_pendiente_m, entry_intercepto_b
    
    pendiente_m = float(entry_pendiente_m.get())
    intercepto_b = float(entry_intercepto_b.get())

    #Graficar la recta
    x = np.linspace(-10, 10, 100) #Valores de X
    y = pendiente_m * x + intercepto_b #Valores de Y
    plt.plot(x, y, color='blue', label="y = {}x + {}".format(pendiente_m, intercepto_b)) #Función de matplotlib para dibujar el trazo
    
    #Graficar los ejes X e Y
    plt.axvline(0, color='black', linewidth=0.5)
    plt.axhline(0, color='black', linewidth=0.5)
    
    #Marcar el punto de intercepcion con el eje Y
    punto_interseccion = (0, intercepto_b)
    plt.scatter(*punto_interseccion, color='blue', label='b = {}'.format(intercepto_b))
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico de la recta y = {}x + {}'.format(pendiente_m, intercepto_b))
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    global entry_pendiente_m, entry_intercepto_b
    
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Gráfico de la Recta")
    ventana.config(bg="#e1d8b9")
    
    # Personalizar el estilo de la ventana
    estilo = ttk.Style()
    estilo.configure("TLabel", font=("Arial", 12))
    estilo.configure("TEntry", font=("Arial", 12))
    estilo.configure("TButton", font=("Arial", 12, "bold"))
    
    # Maximizar la ventana al iniciar
    ventana.state('zoomed')
    
    # Crear etiqueta para la fórmula de la recta
    label_formula = ttk.Label(ventana, text="y = [m]x + [b]", background="#e1d8b9", font=("Arial", 18, "bold"))
    label_formula.pack(pady=10)
    
    # Crear etiqueta y entrada para la pendiente m
    label_pendiente_m = ttk.Label(ventana, text="Pendiente (m):", background="#e1d8b9", font=("bold"))
    label_pendiente_m.pack(pady=10)
    entry_pendiente_m = ttk.Entry(ventana)
    entry_pendiente_m.pack(pady=10)
    
    # Crear etiqueta y entrada para el intercepto b
    label_intercepto_b = ttk.Label(ventana, text="Intercepto (b):", background="#e1d8b9", font=("bold"))
    label_intercepto_b.pack(pady=10)
    entry_intercepto_b = ttk.Entry(ventana)
    entry_intercepto_b.pack(pady=10)
    
    # Crear el botón de "Graficar"
    boton_graficar = ttk.Button(ventana, text="Graficar", command=graficar_recta)
    boton_graficar.pack(pady=10)
    
    # Ejecutar el bucle principal de la ventana
    ventana.mainloop()

if __name__ == "__main__":
    main()
