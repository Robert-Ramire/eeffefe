productos = []

def agregarProducto():
     nombre_producto = input("Ingrese el nombre del producto: ")
     cantidad_producto = input("Ingrese la cantidad del producto: ")
     precio_producto = input("Ingrese el nombre del producto: ")
     productos.append([nombre_producto, cantidad_producto, precio_producto])

def eliminar_producto():
     nombre_producto = input("Ingrese el nombre del producto a eliminar:"):
     global productos

     productos = [producto for producto in productos if producto[0] != nombre_producto]

def actualizar_producto():
     nombre_producto = input("Ingrese el nombre del producto a actualizar: ")
     global productos

     for producto in productos:
          if producto[0] == nombre_producto:
               nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
               nuevo_precio = float(input("Ingrese el nuevo precio: "))

               producto[1]==nueva_cantidad
               producto[2] == nuevo_precio

def buscar_producto():
     nombre_producto = input("Ingrese el nombre del producto a buscar: ")
     global productos

     for producto in productos:
          if producto[0] == nombre_producto:
            print("Producto encontrado")

def valor_total():
     global productos

     for producto in productos:
          total = total + producto[1] * producto[2]

def mostrar_menu():
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Calcular el valor del inventario")
    print("6. Salir")
     
def main():
     while True:
          mostrar_menu()
          opcion = int(input("Ingrese una opcion: "))

          if opcion == 6:
               break
          elif opcion == 1:
               agregarProducto()
          elif opcion == 2:
               actualizar_producto()
          elif opcion == 4:
               buscar_producto()  
          elif opcion == 5:
               valor_total()

if __name__ == "__main__":
     main()

