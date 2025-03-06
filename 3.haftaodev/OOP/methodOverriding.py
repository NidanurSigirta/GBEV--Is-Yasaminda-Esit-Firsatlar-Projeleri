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
        return f"Electric Car: {self.year} {self.brand} {self.model} with a {self.battery_size}-kWh battery"

# Nesne oluşturma
car = Car("Toyota", "Corolla", 2020)
electric_car = ElectricCar("Tesla", "Model 3", 2021, 75)

print(car.car_info())  
print(electric_car.car_info())  

# #Example 2
# class Vehicle:
#     def move(self):
#         print("This vehicle is moving.")

# class Car(Vehicle):
#     def move(self):
#         print("The car is driving on the road.")

# class Boat(Vehicle):
#     def move(self):
#         print("The boat is sailing on the water.")

# # Overriding Testi
# vehicles = [Car(), Boat(), Vehicle()]

# for vehicle in vehicles:
#     vehicle.move()

