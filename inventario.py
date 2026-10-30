class ProductosElectronicos:
    def __init__(self, marca, color, precio, stock):
        self.marca = marca
        self.color = color 
        self.precio = precio
        self.stock = stock


class Telefono(ProductosElectronicos): pass
    
class Laptop(ProductosElectronicos): pass

class Audifonos(ProductosElectronicos): pass

productos = []

while True:
    print("\n---PANEL DE ADMIN: AÑADIR PRODUCTOS---")
    print("1. Telefonos")
    print("2. Laptops")
    print("3. Audifonos")
    print("4. Mostrar productos")
    print("5. Salir")

    opcion = int(input("\nIngresa la opcion de la acción que deseas realizar: "))

    if opcion == 1:
        print("\n--- REGISTRAR TELEFONO ---")
        marca = input("Marca: ")
        color = input("Color: ")
        precio = int(input("Precio: "))
        stock = int(input("Stock: "))

        save1 =  Telefono(marca, color, precio, stock)
        productos.append(save1)

    elif opcion == 2:
        print("\n--- REGISTRAR LAPTOP ---")
        marca = input("Marca: ")
        color = input("Color: ")
        precio = int(input("Precio: "))
        stock = int(input("Stock: "))

        save2 =  Laptop(marca, color, precio, stock)
        productos.append(save2)

    elif opcion == 3: 
        print("\n--- REGISTRAR AUDIFONOS ---")
        marca = input("Marca: ")
        color = input("Color: ")
        precio = int(input("Precio: "))
        stock = int(input("Stock: "))

        save3 =  Audifonos(marca, color, precio, stock)
        productos.append(save3)

    elif opcion == 4:

        for i in productos:
            print(f"\nLos prductos son: Marca: {i.marca} | Precio: {i.precio} | Stcok: {i.stock}")
            
    else:
        print("\nVuelve cuando haya nuevas novendades UwU")
        break

