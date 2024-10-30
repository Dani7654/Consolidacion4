import csv

class GestorArchivos:
    @staticmethod
    def guardar_datos_csv(vehiculos, nombre_archivo='vehiculos.csv'):
        try:
            with open(nombre_archivo, 'w', newline='') as archivo:
                escritor = csv.writer(archivo)
                for vehiculo in vehiculos:
                    escritor.writerow([vehiculo.__class__, vehiculo.__dict__])
            print(f"Datos guardados exitosamente en {nombre_archivo}")
        except Exception as e:
            print(f"Error al guardar los datos: {str(e)}")

    @staticmethod
    def leer_datos_csv(nombre_archivo='vehiculos.csv'):
        from vehiculo import Particular, Carga, Bicicleta, Motocicleta
        vehiculos = []
        try:
            with open(nombre_archivo, 'r') as archivo:
                lector = csv.reader(archivo)
                for fila in lector:
                    clase = eval(fila[0].split("'")[1])
                    atributos = eval(fila[1])
                    vehiculo = clase(**atributos)
                    vehiculos.append(vehiculo)
            
            for tipo in [Particular, Carga, Bicicleta, Motocicleta]:
                print(f"\nLista de Vehiculos {tipo.__name__}")
                for vehiculo in vehiculos:
                    if isinstance(vehiculo, tipo):
                        print(vehiculo.__dict__)
        except Exception as e:
            print(f"Error al leer los datos: {str(e)}")