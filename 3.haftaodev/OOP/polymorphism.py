# Example 1 
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
        return f"{self.year} {self.brand} {self.model} with a {self.battery_size}-kWh battery"

def display_car_info(car):
    print(car.car_info())  

# Objects
regular_car = Car("Toyota", "Corolla", 2020)
electric_car = ElectricCar("Tesla", "Model S", 2021, 100)

display_car_info(regular_car)   
display_car_info(electric_car)     


# # Example 2 
# class Shape:
#     def draw(self):
#         print("Drawing a shape...")

# class Circle(Shape):
#     def draw(self):
#         print("Drawing a Circle...")

# class Square(Shape):
#     def draw(self):
#         print("Drawing a Square...")

# shapes = [Circle(), Square(), Shape()]

# for shape in shapes:
#     shape.draw() 
