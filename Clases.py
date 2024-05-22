class CelularPocoX3Pro:
    def __init__(self, color, pila, almacenamiento, memoria_ram, precio):
        self.color = color
        self.pila = pila
        self.almacenamiento = almacenamiento
        self.memoria_ram = memoria_ram
        self.precio = precio

    def mostrar_info(self):
        print(f"Color: {self.color}")
        print(f"pila: {self.pila} mAh")
        print(f"Almacenamiento: {self.almacenamiento} GB")
        print(f"Memoria RAM: {self.memoria_ram} GB")
        print(f"Precio: ${self.precio}")

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        print(f"El precio se ha actualizado a: ${self.precio}")


mi_celular = CelularPocoX3Pro("negro", 5160, 128, 6, 250)
mi_celular.mostrar_info()
mi_celular.actualizar_precio(230)
