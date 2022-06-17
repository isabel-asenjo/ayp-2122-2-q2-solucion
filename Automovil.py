from Vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, placa, marca, puesto, entrada, minusvalido):
        super().__init__(placa, marca, puesto, entrada)
        self.minusvalido = minusvalido