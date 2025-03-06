#Example 1
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def car_info(self):
        pass

    @abstractmethod
    def wheel_count(self):
        pass

# Class: Car
class Car(Vehicle):
    def __init__(self, brand, model, year, wheels=4):
        self.brand = brand
        self.model = model
        self.year = year
        self.wheels = wheels  # Number of wheels is 4 by default

    def car_info(self):
        return f"{self.year} {self.brand} {self.model}"

    def wheel_count(self):
        return f"{self.brand} {self.model} has {self.wheels} wheels."

# Class: Mercedes (derived from Car)
class Mercedes(Car):
    def __init__(self, model, year, wheels=4):
        super().__init__("Mercedes", model, year, wheels)

# Class: BMW (derived from Car)
class BMW(Car):
    def __init__(self, model, year, wheels=4):
        super().__init__("BMW", model, year, wheels)

#Objects
car = Car("BMW", "5 Series", 2020)
print(car.car_info())
print(car.wheel_count())

mercedes = Mercedes("S-Class", 2022)
print(mercedes.car_info())
print(mercedes.wheel_count())

bmw = BMW("X5", 2021)
print(bmw.car_info())
print(bmw.wheel_count())


# #Example 2
# from abc import ABC, abstractmethod

# class Pet(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass  

# class Dog(Pet):
#     def make_sound(self):
#         print("Bark! Bark!")

# class Cat(Pet):
#     def make_sound(self):
#         print("Meow! Meow!")

# pets = [Dog(), Cat()]

# for pet in pets:
#     pet.make_sound()

