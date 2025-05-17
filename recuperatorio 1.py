#recuperatiorio parcial 1 programacion I Adriel Lopez

# puede iniciar el programa con las listas vacias
# e ir cargando productos y cantidades o usar estas listas ya cargadas:

#lista_productos=[]
#lista_cantidades=[]

lista_productos=["panes", "leches", "arroz", "fideos", "jugos", "gaseosas", "carnes","caramelos"]
lista_cantidades=[10, 5, 0, 20, 8, 0, 13, 121]

print("""Menú de opciones:
1. Agregar producto
2. Ver productos agotados
3. Actualizar stock
4. Ver todos los productos
5. Salir""")

while True:
    
    opc= int(input("Ingrese el numero de opcion a realizar: "))

    if opc==1:
        productoNew= input("ingrese el nuevo producto a la lista: ")
        lista_productos.append(productoNew)
        
        cantidad = int(input("Ingrese la cantidad disponible de este producto: "))
        lista_cantidades.append(cantidad)
        
        print("Listo producto agregado!\n Producto:",productoNew ,"\n cantidad:", cantidad)
        
    elif opc==2:
        print("Los productos agotados son:")
        
        for i in range(len(lista_cantidades)):
            if lista_cantidades[i] == 0:
                print(lista_productos[i])
                
    elif opc==3:
        productoUpdate = int(input("Ingrese el nombre del producto a actualizar: "))
    
        for i in range(len(lista_productos)):
            if lista_productos[i] == productoUpdate:
                
                cantidadUpdate = int(input("Ingrese la nueva cantidad de ",{productoUpdate},":"))
                lista_cantidades[i] = cantidadUpdate 
                print(f"Stock de '{productoUpdate}' actualizado a {cantidadUpdate}.\n")
                break 
             
            else:
                print("error intente de nuevo.\n Los productos disponibles son", lista_productos)
                break
                
    elif opc==4:
        print("Listado de productos y sus cantidades:")
        
        for i in range (len(lista_productos)):
            print(lista_productos[i],"tiene",lista_cantidades[i],"unidades")
    
    elif opc==5:
        print("FIN DEL PROYECTO")
        break
    
    else:
        print("Opción inválida. Por favor, ingrese una opción entre 1 y 5.")
