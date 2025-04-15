# 'owns a' relationship
class Engine:
    def __init__(self, hoursepower):
        self.hoursepower = hoursepower


class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, hourse_power, wheel_size):
        self.make = make 
        self.model = model
        self.engine = Engine(hourse_power)
        self.wheel = Wheel(wheel_size)
        self.wheel = [Wheel(wheel_size) for _ in range(4)] 
        
    def __str__(self):
        return f"{self.make} {self.model} with {self.engine.hoursepower} HP and {self.wheel[0].size} inch wheels." 
car = Car("Ford", "Mustang", 450, 18)
print(car.__str__())