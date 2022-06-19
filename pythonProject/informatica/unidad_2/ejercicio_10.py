productos = ["té", "café", "arroz", "harina 000", "lata de tomate", "jabón", "queso pategras", "leche", "levadura",
"desodorante", "detergente", "agua con gas", "trapo de piso", "lavandina", "aceite de oliva", "vinagre",
"mayonesa", "ketchup", "galletas de arroz"]

def producto_buscado(producto):
    if producto in productos:
        print ("Producto en existencia:", producto)
    else:
        print("El proveedor no cuenta con el producto:", producto)

producto_buscado("café")
producto_buscado("oro")