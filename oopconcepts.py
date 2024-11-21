class Vehicle:
    def __init__(self, color, max_speed):
        self.__color = color; # Encapsulation: Private variable for color
        self.__max_speed = max_speed;  # Encapsulation: Private variable for max speed

    def get_color(self):
        return self.__color;

    def set_color(self, color):
        self.__color = color;

    def get_max_speed(self):
        return self.__max_speed;

    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed;

    def move(self):
        print("Vehicle is moving...")


class Car(Vehicle):  # Inheritance: Car inherits from Vehicle
    def __init__(self, color, max_speed, num_doors):
        super().__init__(color, max_speed)  # Inherit properties from Vehicle
        self.__num_doors = num_doors;

    def get_num_doors(self):
        return self.__num_doors

    def move(self):  # Polymorphism: Overriding the move method
        print("Car is moving on the road...");


class Bike(Vehicle):  # Inheritance: Bike inherits from Vehicle
    def __init__(self, color, max_speed, has_basket):
        super().__init__(color, max_speed)
        self.__has_basket = has_basket;

    def has_basket(self):
        return self.__has_baske

    def move(self):  # Polymorphism: Overriding the move method
        print("Bike is moving on the street...")


# Abstract class for vehicles
from abc import ABC, abstractmethod

class VehicleAbstract(ABC):
    @abstractmethod
    def move(self):
        pass


# Concrete vehicle class implementing the abstract class
class ConcreteVehicle(VehicleAbstract):
    def move(self):
        print("Concrete vehicle is moving...");