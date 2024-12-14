import almacen

class Filamento:
    def __init__(self, tipo, color, cantidad):
        self.tipo=tipo
        self.color=color
        self.cantidad=cantidad

    def __str__(self):
        return f"Tipo: {self.tipo}, Color: {self.color}, Cantidad: {self.cantidad}"
    

def mostrar_menu():
    print("\nMenú de Almacén:")
    print("1. Registrar nuevo filamento")
    print("2. Listar todos los filamentos")
    print("3. Buscar filamentos por tipo")
    print("4. Buscar filamentos por color")
    print("5. Salir")

def main():
    from almacen import Almacen
    almacen=Almacen()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Ingrese el tipo de filamento: ")
            color = input("Ingrese el color del filamento: ")
            cantidad = int(input("Ingrese la cantidad: "))
            almacen.agregar_filamento(tipo, color, cantidad)
            print("Filamento registrado con éxito.")
        elif opcion == "2":
            almacen.listar_filamentos()
        elif opcion == "3":
            tipo = input("Ingrese el tipo a buscar: ")
            resultados=almacen.buscar_por_tipo(tipo)
            for filamento in resultados:
                print(filamento)
        elif opcion == "4":
            color = input("Ingrese el color a buscar: ")
            resultados = almacen.buscar_por_color(color)
            for filamento in resultados:
                print(filamento)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()

    







