import random

class Car:
    def __init__(self, speed):
        self.speed = speed

    def __repr__(self):
        return f"Car with {self.speed} km/h Speed"

# Create 5 cars with random speeds
cars = [Car(random.randint(60, 200)) for i in range(5)]

print("Random cars:")
print(cars)
print()

def car_speed(car):
    """Returns the speed of the car"""
    return car.speed

print(f"Speed of first car: {car_speed(cars[0])}")
print()

fastest_car = max(cars, key=car_speed)
print(f"Fastest Car: {fastest_car}")