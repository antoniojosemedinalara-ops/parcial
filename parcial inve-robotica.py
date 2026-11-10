inventario=[]
producto={
    "ID":"",
    "nombre":"",
    "categoria":"",
    "stock": 0,
    "precio_unitario": 0.0
}

while True:

    print("/////MENU-INVENTARIO/////")
    print("1. Registrar componentes")
    print("2. Consultar y filtrar")
    print("3. Actualizar stock")
    print("4.Salir")

    opcion=int(input("Que desea realizar?: "))

    match opcion:
        case 1:
            producto["ID"]=input("Ingrese el ID del producto: ")
            producto["nombre"]=input("Ingrese el nombre del producto: ")
            producto["categoria"]=input("Ingrese la categoria del producto: ")
            producto["stock"]=int(input("Ingrese el stock del producto: "))
            producto["precio_unitario"]=float(input("Ingrese el precio unitario del producto: "))
            inventario.append(producto.copy())
            print("Producto registrado con exito")
        case 2:
            print("/////CONSULTA Y FILTRO/////")
            print("1. Consultar por categoria")
            print("2. Consultar por ID")
            print("3. Consultar por nombre")
            opcion_consulta=int(input("Que desea realizar?: "))
            if len(inventario)!=0:
                match opcion_consulta:
                    case 1:
                        categoria=input("Ingrese la categoria a consultar: ")
                        for prod in inventario:
                            if prod["categoria"]==categoria:
                                print(prod)
                    case 2:
                        id_producto=input("Ingrese el ID a consultar: ")
                        encontrado=False
                        for prod in inventario:
                            if prod["ID"]==id_producto:
                                print(prod)
                                encontrado=True
                        if not encontrado:
                            print("No se encontro el producto con el ID ingresado")
                    case 3:
                        nombre_producto=input("Ingrese el nombre a consultar: ")
                        for prod in inventario:
                            if prod["nombre"]==nombre_producto:
                                print(prod)
                    case _:
                        print("opcion invalida, por favor intente de nuevo")
            else:
                print("No hay productos registrados en el inventario")
        case 3: 
            id_producto=input("Ingrese el ID del producto a actualizar stock: ")
            for prod in inventario:
                if prod["ID"]==id_producto:
                    nuevo=int(input("Ingrese el nuevo stock(si desea restar, use una cantidad negativa): "))
                    nuevo_stock=prod["stock"]+ nuevo
                    if nuevo_stock<0:

                        print("no se puede actualizar el stock, la cantidad es menor a 0")
                    else:
                        prod["stock"]=nuevo_stock
                    print("Stock actualizado con exito")
            else:
                print("No hay productos registrados en el inventario")
        case 4:
            print("Saliendo del programa...")
            break
        case _:
            print("opcion invalida, por favor intente de nuevo")
