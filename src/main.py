#!/usr/bin/env python3

# Se importa el módulo tkinter para la interfaz
import tkinter as tk

# Crea la ventana principal y define sus propiedades
ventana_principal = tk.Tk()
ventana_principal.geometry("600x700")
ventana_principal.resizable(False, False)
ventana_principal.configure(background="#9B9B9B")
ventana_principal.title("Resolución de Sudoku")

# Crea el frame principal y define sus propiedades
frame_principal = tk.Frame(
    ventana_principal,
    width="600",
    height="700",
)
frame_principal.configure(background="#FAFAFA")
frame_principal.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Crea el canvas principal y define sus propiedades
canvas_principal = tk.Canvas(
    frame_principal,
    width="600",
    height="700",
    highlightthickness=3,
    highlightbackground="#000000",
)
canvas_principal.configure(background="#FAFAFA")
canvas_principal.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Se define una matriz para los valores a manejar por el algoritmo
valores = []

# Se recorre todas las columnas del array para añadir las filas
# Esto se hace así para poder acceder a los métodos set y get
for i in range(1, 10):
    valores += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
for i in range(0, 9):
    for j in range(0, 9):
        valores[i][j] = tk.StringVar(ventana_principal)

# Se define una función, la cuál define todos los valores de las casillas vacías en 0 e inicia el algoritmo de vuelta atrás para buscar la solución
def resolver_sudoku():
    llenar_cuadricula()
    empezar_solucion()


# Lee los valores de toda la matriz y si alguno es un número no válido, lo define como un cero
def llenar_cuadricula():
    for i in range(9):
        for j in range(9):
            if valores[i][j].get() not in [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
            ]:
                valores[i][j].set(0)


# Se define la función que busca a la celda más cercana que se encuentre vacía
def hallar_casilla_vacia(i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if valores[x][y].get() == "0":
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if valores[x][y].get() == "0":
                return x, y
    return -1, -1


# Se define la función que verifica qué números se encuentran disponibles para utilizarse dada una casilla en especifico
def verificar_numero(i, j, e):
    for x in range(9):
        # Verifica si el número se encuentra en la misma fila
        if valores[i][x].get() == str(e):
            return False
    for x in range(9):
        # Verifica si el número se encuentra en la misma columna
        if valores[x][j].get() == str(e):
            return False
    cuadricula_horizontal, cuadricula_vertical = 3 * int((i / 3)), 3 * int((j / 3))
    for x in range(cuadricula_horizontal, cuadricula_horizontal + 3):
        for y in range(cuadricula_vertical, cuadricula_vertical + 3):
            # Verifica si el número está en la misma cuadricula
            if valores[x][y].get() == str(e):
                return False
    # Si devuelve verdadero es porque el número se puede utilizar en la casilla
    return True


# Se define la función que implementa el algoritmo de vuelta atrás
# Se empieza definiendo una posición inicial en el origen de la matriz es decir de cero y cero
def empezar_solucion(i=0, j=0):
    i, j = hallar_casilla_vacia(i, j)
    # Si i es igual a menos uno el sudoku ya está resuelto porque no tiene ninguna casilla vacía
    if i == -1:
        return True
    for e in range(1, 10):
        if verificar_numero(i, j, e):
            valores[i][j].set(e)
            # Se vuelve a llamar a la función recursivamente para que se ejecute hasta que solucione el sudoku
            if empezar_solucion(i, j):
                # Si se devuelve verdadero es porque el sudoku acaba de ser resuelto y el "ciclo" puede terminar
                return True
            # Se devuelve una posición por la raíz del grafo
            valores[i][j].set(0)
    # Si se devuelve falso es porque la configuración dada para el sudoku no tiene solución
    return False


# Se define la función que recorre toda la matriz y reinicia los valores de cada casilla
def borrar():
    for i in range(9):
        for j in range(9):
            valores[i][j].set("")


# Crea una label y define sus propiedades
titulo_proyecto = tk.Label(ventana_principal, text="Resolución de Sudoku")
titulo_proyecto.config(background="#9B9B9B", font=("Arial", 16, "bold"))
titulo_proyecto.place(x=300, y=50, anchor=tk.CENTER)

# Se define una matriz del mismo tamaño para las casillas de texto mostradas en la interfaz
cuadricula = []

# Se recorre todas las columnas del array para añadir las filas
# Esto se hace así para poder acceder a los métodos set y get
for i in range(1, 10):
    cuadricula += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
for i in range(0, 9):
    for j in range(0, 9):
        cuadricula[i][j] = tk.Entry(
            frame_principal,
            width=2,
            font=("Arial", 18),
            bg="white",
            cursor="arrow",
            borderwidth=0,
            highlightcolor="yellow",
            highlightthickness=1,
            highlightbackground="black",
            textvar=valores[i][j],  # type: ignore
        )
        # Se especifica un padding interno para aumentar el tamaño de las casillas
        cuadricula[i][j].grid(row=i, column=j, ipadx=12, ipady=12)

# Crea un botón y define sus propiedades
boton_resolver = tk.Button(
    ventana_principal,
    text="Resolver",
    font=("Arial", 16, "bold"),
    command=resolver_sudoku,
)
boton_resolver.place(x=180, y=650, anchor=tk.CENTER)

# Crea un botón y define sus propiedades
boton_borrar = tk.Button(
    ventana_principal, text="Borrar", font=("Arial", 16, "bold"), command=borrar
)
boton_borrar.place(x=300, y=650, anchor=tk.CENTER)

# Crea un botón y define sus propiedades
boton_salir = tk.Button(
    ventana_principal,
    text="Salir",
    font=("Arial", 16, "bold"),
    command=ventana_principal.quit,
)
boton_salir.place(x=400, y=650, anchor=tk.CENTER)

# Utiliza el método mainloop nativo del módulo tkinter para detener la alocación de recursos
ventana_principal.mainloop()
