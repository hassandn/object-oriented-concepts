from student import Student

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student3 = Student("Charlie", 23)
print(student1.year)  
print(student1.name)
print(student1.age)
print(Student.year)  # Accessing class variable through the class name and we can say that it is a class variable
print(Student.number_of_students)
print(student1.how_many_students_we_are())  # Accessing the method of the class
