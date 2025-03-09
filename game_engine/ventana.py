import tkinter as tk

class Ventana:
    def __init__(self, titulo, ancho, alto):
        self.ventana = tk.Tk()
        self.ventana.title(titulo)
        self.canvas = tk.Canvas(self.ventana, width=ancho, height=alto)
        self.canvas.pack()

    def mostrar(self):
        self.ventana.mainloop()