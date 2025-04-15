
# class is a blueprint for creating objects
class Car:
# init is a constructor method that initializes the object
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"The {self.color} {self.model} is driving.")
    
    def stop(self):
        print(f"you stopped the {self.color} {self.model}.")    
        
    def describe(self):
        print(f"this is a {self.color} {self.model} from {self.year}.")
    