class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def main():
    vehicle_type = "car"
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sunroof): ")

    car = Automobile(vehicle_type, year, make, model, doors, roof)

    print("\nVehicle details:")
    print(f" Vehicle type: {car.vehicle_type}")
    print(f" Year: {car.year}")
    print(f" Make: {car.make}")
    print(f" Model: {car.model}")
    print(f" Number of doors: {car.doors}")
    print(f" Roof type: {car.roof}")

if __name__ == "__main__":
    main()