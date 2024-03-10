import random

class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance_covered = 0

    def drive(self):
        self.distance_covered += self.speed

    def __str__(self):
        return f"{self.name:<15} | {self.distance_covered:8} km"


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.speed += random.randint(-5, 5)
            car.drive()

    def print_status(self):
        print(f"\nCurrent status of cars in the {self.name} race:")
        print("Car Name        | Distance Covered")
        for car in self.cars:
            print(car)


    def race_finished(self):
        for car in self.cars:
            if car.distance_covered >= self.distance:
                return True
        return False


def main():
    car_list = [Car(f"Car {i}", random.randint(60, 150)) for i in range(1, 11)]
    grand_demolition_derby = Race("Grand Demolition Derby", 5000, car_list)

    hours = 0
    while not grand_demolition_derby.race_finished():
        if hours % 10 == 0:
            grand_demolition_derby.print_status()
        grand_demolition_derby.hour_passes()
        hours += 1

    grand_demolition_derby.print_status()
    print(f"\nThe race is finished after {hours} hours!")

if __name__ == "__main__":
    main()
