#Example 1
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        return f"{self.year} {self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size):
        super().__init__(brand, model, year)
        self.battery_size = battery_size

    def car_info(self):
        return f"{super().car_info()} with a {self.battery_size}-kWh battery"


electric_car = ElectricCar("Tesla", "Model 3", 2022, 75)
print(electric_car.car_info()) 


# #Example 2
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def make_sound(self):
#         print("Some generic animal sound...")

# # The Dog class derives from Animal
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name, "Dog")
#         self.breed = breed

#     def make_sound(self):
#         print("Woof woof!")

# # The Cat class derives from Animal
# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name, "Cat")  # species

#     def make_sound(self):
#         print("Meow meow!")

# dog1 = Dog("Buddy", "Golden Retriever")
# dog1.make_sound()  # Woof woof!

# cat1 = Cat("Mia")
# cat1.make_sound()  # Meow meow!

