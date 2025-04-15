class Student:
    year = 1  # class variable
    number_of_students = 0  # class variable
        
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.number_of_students += 1  # Increment the number of students when a new student is created
        
    def how_many_students_we_are(self):
        return f"There are {Student.number_of_students} students in the class {Student.year}."
