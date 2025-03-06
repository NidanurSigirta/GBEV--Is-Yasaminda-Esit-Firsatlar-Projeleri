#Example 1
class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand 
        self.model = model
        self.year = year

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand


car = Car("Volvo", "XC90 ", 2020)
print(car.get_brand()) 
car.set_brand("Audi")
print(car.get_brand()) 

# #Example 2
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.__balance = balance  # Private 

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited {amount}, new balance: {self.__balance}")
#         else:
#             print("Invalid deposit amount!")

#     def get_balance(self):
#         return self.__balance 
    
# account = BankAccount("TR123456789", 5000)
# account.deposit(1000)
# print("Current balance:", account.get_balance())

