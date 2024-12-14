import json

class Filamento:
    def __init__(self, tipo, color, cantidad):
        self.tipo = tipo
        self.color = color
        self.cantidad = cantidad

    def __str__(self):
        return f"Tipo: {self.tipo}, Color: {self.color}, Cantidad: {self.cantidad}"

class Almacen:
    def __init__(self):
        self.filamentos = []

    def agregar_filamento(self, tipo, color, cantidad):
        self.filamentos.append(Filamento(tipo, color, cantidad))

    def listar_filamentos(self):
        for filamento in self.filamentos:
            print(filamento)

    def guardar_datos(self, archivo="almacen.json"):
        with open(archivo, "w") as f:
            
            json.dump([filamento.__dict__ for filamento in self.filamentos], f, indent=4)

    def cargar_datos(self, archivo="almacen.json"):
        try:
            with open(archivo, "r") as f:
                data = json.load(f)
                self.filamentos = [Filamento(**filamento) for filamento in data]
        except FileNotFoundError:
            print("No se encontraron datos previos.")


def main():
    almacen = Almacen()

    almacen.cargar_datos()

    almacen.agregar_filamento("PLA", "Rojo", 100)
    almacen.agregar_filamento("ABS", "Azul", 50)

    almacen.listar_filamentos()

    almacen.guardar_datos()

if __name__ == "__main__":
    main()
