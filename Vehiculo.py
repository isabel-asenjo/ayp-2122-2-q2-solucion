class Vehiculo:
    def __init__(self, placa, marca, puesto, entrada):
        self.placa = placa
        self.marca = marca
        self.puesto = puesto
        self.entrada = entrada
        self.salida = '-'

    def mostrar(self):
        print(f"--- {self.placa} ------\n\t- Marca: {self.marca}\n\t- Puesto: {self.puesto}\n\t- Hora de entrada: {self.entrada}\n\t- Hora de salida: {self.salida}")