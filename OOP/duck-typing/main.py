# if its looks like a duck and quacks like a duck, it must be a duck

class Animal:
    alive = True
    

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")
        

class Cat(Animal):
    def speak(self):
        print("Meow! Meow!")
        
# it has minimum requirements to be considered an animal
class Car:
    def speak(self):
        print("Vroom! Vroom!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()