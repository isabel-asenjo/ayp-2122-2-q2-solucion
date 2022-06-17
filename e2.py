from datetime import datetime
from Automovil import Automovil
from Motocicleta import Motocicleta

def read_txt(file):
    try:
        with open(file) as db:
            data = db.readlines()
        return data
    except FileNotFoundError:
        print("Este archivo no existe.")


def save_data(vehicles):
    data = []
    for v in vehicles:
        if type(v) == Automovil:
            data.append(f"AUTOMOVIL|{v.placa}|{v.marca}|{v.puesto}|{v.entrada}|{v.salida}|{v.minusvalido}\n")
        else:
            data.append(f"MOTOCICLETA|{v.placa}|{v.marca}|{v.puesto}|{v.entrada}|{v.salida}\n")

    with open("updatedParkingLot.txt", "w") as file:
        file.writelines(data)


def load_vehicles(data):
    vehicles = []
    for v in data:
        vehicle = v[:-1].split("|")
        if vehicle[0] == "AUTOMOVIL":
            vehicles.append(Automovil(vehicle[1], vehicle[2], vehicle[3], vehicle[4], vehicle[5]))
        else:
            vehicles.append(Motocicleta(vehicle[1], vehicle[2], vehicle[3], vehicle[4]))

    return vehicles


def show_vehicles(vehicles):
    for i,v in enumerate(vehicles):
        if v.puesto != "-":
            v.mostrar()


def vehicle_exit(vehicles):
    current_vehicles = []
    for v in vehicles:
        if v.puesto != "-":
            current_vehicles.append(v)

    for i,v in enumerate(current_vehicles):
        print("---",i+1)
        if v.puesto != "-":
            v.mostrar()
    vehicle_number = input("Ingrese el número correspondiente al vehículo que saldrá: ")
    while not vehicle_number.isnumeric() or int(vehicle_number) not in range(1,len(vehicles)+1):
        vehicle_number = input("Ingreso inválido, ingrese el número correspondiente al vehículo que saldrá: ")
    
    vehicle = vehicles[int(vehicle_number)-1]
    vehicle.puesto = "-"
    now = datetime.now()
    vehicle.salida = now.strftime("%H:%M:%S")

    print(f"El vehículo de placa {vehicle.placa} ha salido a las {vehicle.salida}")


def main():
    vehicles = load_vehicles(read_txt("parkingLot.txt"))
    while True:
        print("------ ADMINISTRADOR DE ESTACIONAMIENTO ------")
        print("1. Ver vehículos\n2. Registrar salida\n3. Cerrar programa")
        s = input("Ingrese el número correspondiente a su elección: ")
        while s != "1" and s != "2" and s != "3":
            s = input("Ingreso inválido, ingrese el número correspondiente a su elección: ")

        print()

        if s == "1":
            show_vehicles(vehicles)
        elif s == "2":
            vehicle_exit(vehicles)
        else:
            save_data(vehicles)
            print("¡Hasta luego!")
            break

        print()

main()