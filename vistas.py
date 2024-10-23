import tkinter as tk
from tkinter import Canvas, ttk
import requests
from PIL import Image, ImageTk

indice = 0  # Define el índice global para navegar entre productos
data = None  # Definir una variable global para 'data'

def mostrar_productos(productos_data):
    global data, root, canvas, nombre, tags, descripcion, categoria, marca, precio, rating, warranty, stock, compra_llega, sku, img_tk, search_entry

    # Asignamos 'productos_data' a la variable global 'data'
    data = productos_data

    root = tk.Tk()
    root.title("Productos")
    root.resizable(width=False, height=False)
    root.geometry("751x600")

    search_label = tk.Label(root, text="Buscar por título:",font=('inter',15))
    search_label.pack(pady=10)
    search_entry = tk.Entry(root, width=50)
    search_entry.pack(pady=5)
    search_button = ttk.Button(root, text="Buscar", command=buscar_producto)
    search_button.pack(pady=5)

    canvas = tk.Canvas(root, width=530, height=751, background='Orange')
    canvas.pack(fill="both", expand=True)

    nombre = canvas.create_text(150, 36, anchor="nw", font=('inter', 20))
    tags = canvas.create_text(150, 65, anchor="nw", font=('inter', 10))
    descripcion = canvas.create_text(150, 80, anchor="nw", width=550, font=('inter', 10))
    categoria = canvas.create_text(740, 5, anchor="ne", font=('inter', 8))
    marca = canvas.create_text(740, 175, anchor="ne", font=('inter', 15))
    precio = canvas.create_text(50, 175, anchor="nw", font=('inter', 15))
    rating = canvas.create_text(50, 225, anchor="nw", font=('inter', 15))
    warranty = canvas.create_text(50, 275, anchor="nw", font=('inter', 15))
    stock = canvas.create_text(50, 325, anchor="nw", font=('inter', 15))
    compra_llega = canvas.create_text(740, 275, anchor="ne", font=('inter', 15))
    sku = canvas.create_text(400, 450, anchor="center", font=('inter', 15))

    boton_siguiente = ttk.Button(root, text="Siguiente", command=siguiente)
    boton_siguiente.place(x=600, y=500, anchor="center", width=150)

    boton_anterior = ttk.Button(root, text="Anterior", command=anterior)
    boton_anterior.place(x=200, y=500, anchor="center", width=150)

    mostrar_informacion_producto()  # Muestra el primer producto al iniciar

    root.mainloop()

def siguiente():
    global indice
    if indice < len(data.products) - 1:  # Aumenta el índice si no es el último producto
        indice += 1
        mostrar_informacion_producto()

def anterior():
    global indice
    if indice > 0:
        indice -= 1
        mostrar_informacion_producto()

def mostrar_informacion_producto():
    global canvas, nombre, tags, descripcion, categoria, marca, precio, rating, warranty, stock, compra_llega, sku, img_tk

    producto = data.products[indice]

    canvas.itemconfig(nombre, text=producto.title)
    canvas.itemconfig(tags, text=producto.tags)
    canvas.itemconfig(descripcion, text=producto.description)
    canvas.itemconfig(categoria, text=producto.category)
    canvas.itemconfig(marca, text=producto.brand)
    canvas.itemconfig(precio, text=producto.price)
    canvas.itemconfig(rating, text=producto.rating)
    canvas.itemconfig(warranty, text=producto.warranty_information)
    canvas.itemconfig(stock, text=producto.stock)
    canvas.itemconfig(compra_llega, text=producto.shipping_information)
    canvas.itemconfig(sku, text=producto.sku)


    r = requests.get(producto.thumbnail, stream=True)
    img_data = r.raw
    imag = Image.open(img_data).resize((150, 150))
    img_tk = ImageTk.PhotoImage(imag)
    canvas.create_image(0, 0, image=img_tk, anchor="nw")
    canvas.image = img_tk

def buscar_producto():
    global indice
    busqueda = search_entry.get().lower()  # Obtiene el texto ingresado y lo convierte a minúsculas

    contador = 0  # Inicializamos un contador manualmente

    # Recorremos la lista de productos
    for producto in data.products:
        if busqueda in producto.title.lower():
            indice = contador  # Asignamos el valor del contador al índice
            mostrar_informacion_producto()
            return
        contador += 1  # Incrementamos el contador manualmente en cada iteración

    print("Producto no encontrado")






