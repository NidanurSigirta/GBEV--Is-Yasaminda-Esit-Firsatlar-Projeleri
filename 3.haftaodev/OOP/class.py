# Example 1
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def car_info(self):
        return f"{self.year} {self.brand} {self.model}"

car1 = Car("Mercedes-Benz", "G", 2025)
print(car1.car_info()) 

# #Example 2
# class Account:
#     def __init__(self, account_no, full_name, balance):
#         self.account_no = account_no
#         self.full_name = full_name
#         self.balance = balance

#     def display_balance(self):
#         print(f"Account Holder: {self.full_name}")
#         print(f"Account Number: {self.account_no}")
#         print(f"Balance: {self.balance}")

# account_1 = Account("502edec2-e13e-48fd-8ce7-3dff4eda3c39", "Nidanur Sıgırta", 2000)
# account_1.display_balance()


# #Example 3
# class Student:
#     def __init__(self, name, student_id, major):
#         self.name = name
#         self.student_id = student_id
#         self.major = major

#     def introduce(self):
#         print(f"Hello, my name is {self.name}. My student ID is {self.student_id} and I am studying {self.major}.")

# student1 = Student("Nidanur Sıgırta", "20231045", "Computer Engineering")
# student1.introduce()
