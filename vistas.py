import tkinter as tk
from tkinter import Label,Canvas

import requests
from PIL import Image, ImageTk

indice=0



def mostrar_productos(data):
    root = tk.Tk()
    #for producto in data.products:
    #    label = tk.Label(root, text=producto.title)
    #    label.pack()
    root.title("Productos")
    root.resizable(width=False, height=False)
    root.geometry("751x530")
    canvas = tk.Canvas(root, width=530, height=751, background='Orange')
    canvas.pack(fill="both", expand=True)

    nombre = canvas.create_text(150,36,anchor="nw", font=('inter', 20), text=data.products[indice].title)
    tags = canvas.create_text(150,65,anchor="nw", font=('inter', 10), text=data.products[indice].tags)
    descripcion = canvas.create_text(150,80,anchor="nw",width=550, font=('inter', 10), text=data.products[indice].description)
    categoria = canvas.create_text(740,5,anchor="ne", font=('inter', 8), text=data.products[indice].category)
    marca = canvas.create_text(740,175,anchor="ne", font=('inter', 15), text=data.products[indice].brand)
    precio = canvas.create_text(50,175,anchor="nw", font=('inter', 15), text=data.products[indice].price)
    rating = canvas.create_text(50,225,anchor="nw", font=('inter', 15), text=data.products[indice].rating)
    warranty = canvas.create_text(50,275,anchor="nw", font=('inter', 15), text=data.products[indice].warranty_information)
    stock = canvas.create_text(50,275,anchor="nw", font=('inter', 15), text=data.products[indice].stock)
    compra_llega = canvas.create_text(740,275,anchor="ne", font=('inter', 15), text=data.products[indice].shipping_information)
    sku = canvas.create_text(375,450,anchor="center", font=('inter', 15), text=data.products[indice].sku)

    r = requests.get(data.products[indice].thumbnail,stream=True)
    img_data = r.raw
    imag = Image.open(img_data).resize((200,200))
    img_tk = ImageTk.PhotoImage(imag)
    canvas.create_image(0,0,image=img_tk,anchor="nw")




    root.mainloop()

    # r=request.get(URL,stream=True)
    #img = image.open.rrau
    #imagettk = Imagettk(img)