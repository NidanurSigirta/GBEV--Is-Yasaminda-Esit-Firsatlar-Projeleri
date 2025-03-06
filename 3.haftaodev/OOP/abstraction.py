#Example 1
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def car_info(self):
        pass

class Car(Vehicle):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        return f"{self.year} {self.brand} {self.model}"

car = Car("BMW", "5 Series", 2020)
print(car.car_info())  


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

