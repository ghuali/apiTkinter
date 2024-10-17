import tkinter as tk

def mostrar_productos(data):
    root = tk.Tk()
    for producto in data.products:
        label = tk.Label(root, text=producto.title)
        label.pack()

    root.mainloop()