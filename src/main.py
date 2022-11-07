#!/usr/bin/env python3
import tkinter as tk
from funciones import resolver_sudoku

ventana_principal = tk.Tk()
ventana_principal.geometry("1280x720")
ventana_principal.resizable(False, False)
ventana_principal.configure(background="#4DBFD9")
ventana_principal.title("Resolución de Sudoku")

frame_principal = tk.Frame(
    ventana_principal,
    width="1120",
    height="540",
    highlightthickness=5,
    highlightbackground="#4D4D4D",
)
frame_principal.configure(background="#FAFAFA")
frame_principal.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

canvas_principal = tk.Canvas(
    frame_principal,
    width="1024",
    height="576",
    highlightthickness=0,
    highlightbackground="#4D4D4D",
)
canvas_principal.configure(background="#FAFAFA")
canvas_principal.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

# titulo_proyecto = tk.Label(ventana_principal, text="Resolución de Sudoku")
# titulo_proyecto.config(background="#4DBFD9", font=("Arial", 16, "bold"))
# titulo_proyecto.place(x=550, y=50)

# logo = tk.PhotoImage(file="logo.png")
# logo_label = tk.Label(ventana_principal, background="#4DBFD9", image=logo)
# logo_label.place(x=1000, y=15)

# cuadricula = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]

# Agregar for que cree todas las casillas 9x9 = 81 casillas / 3 bloques por lado
for coordenada_x in range(0, 360, 40):
    for coordenada_y in range(0, 360, 40):
        tk.Entry(ventana_principal).place(
            x=coordenada_x, y=coordenada_y, width=40, height=40
        )

# Agregar botón
ventana_principal.mainloop()

# def set_text(text):
#     e.delete(0,END)
#     e.insert(0,text)
#     return
#
# win = Tk()
#
# e = Entry(win,width=10)
# e.pack()
#
# b1 = Button(win,text="animal",command=lambda:set_text("animal"))
# b1.pack()
# boton que muestre la respuesta
# messagebox.askyesno("Resultado", "La solucionn de la dialectica")

# if resolver_sudoku(cuadricula):
#     for i in range(9):
#         for j in range(9):
#             print(cuadricula[i][j], end=" "),
#         print()
# else:
#     print("No existe solución!")
#
