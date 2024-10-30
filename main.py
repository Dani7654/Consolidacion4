from vehiculo import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta
from gestor_archivos import GestorArchivos

class SistemaVehiculos:
    def __init__(self):
        self.particular = None
        self.carga = None
        self.bicicleta = None
        self.motocicleta = None
        self.vehiculos = []

    def crear_instancias(self):
        """Crea las instancias de los diferentes tipos de vehículos"""
        self.particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
        self.carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
        self.bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
        self.motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)
        self.vehiculos = [self.particular, self.carga, self.bicicleta, self.motocicleta]

    def guardar_vehiculos(self):
        """Guarda los vehículos en el archivo CSV"""
        GestorArchivos.guardar_datos_csv(self.vehiculos)

    def leer_vehiculos(self):
        """Lee los vehículos del archivo CSV"""
        GestorArchivos.leer_datos_csv()

    def verificar_relaciones(self):
        """Verifica las relaciones de instancia para la motocicleta"""
        print("\nVerificando relaciones de instancia para motocicleta:")
        print(f"Motocicleta es instancia con relación a Vehiculo: {isinstance(self.motocicleta, Vehiculo)}")
        print(f"Motocicleta es instancia con relación a Automovil: {isinstance(self.motocicleta, Automovil)}")
        print(f"Motocicleta es instancia con relación a Vehiculo particular: {isinstance(self.motocicleta, Particular)}")
        print(f"Motocicleta es instancia con relación a Vehiculo de Carga: {isinstance(self.motocicleta, Carga)}")
        print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(self.motocicleta, Bicicleta)}")
        print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(self.motocicleta, Motocicleta)}")

    def ejecutar(self):
        """Método principal que ejecuta todas las operaciones del sistema"""
        self.crear_instancias()
        self.guardar_vehiculos()
        self.leer_vehiculos()
        self.verificar_relaciones()

if __name__ == "__main__":
    sistema = SistemaVehiculos()
    sistema.ejecutar()