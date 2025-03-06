#Example 1
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def book_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")

book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)

book1.book_info()
book2.book_info()

# #Examle 2
# class Student:
#     def __init__(self, name, student_id, major, gpa=0.0):
#         self.name = name
#         self.student_id = student_id
#         self.major = major
#         self.gpa = gpa  # Defaults to 0.0

#     def display_info(self):
#         print(f"Ad: {self.name}, Öğrenci No: {self.student_id}, Bölüm: {self.major}, Not Ortalaması: {self.gpa}")

# student1 = Student("Ahmet Yılmaz", "20231001", "Bilgisayar Mühendisliği", 3.5)
# student2 = Student("Zeynep Demir", "20231002", "Elektrik-Elektronik Mühendisliği")

# student1.display_info()
# student2.display_info()
