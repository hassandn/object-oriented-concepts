from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    def go(self):
        print("The car is going.")
    
    def stop(self):
        print("The car has stopped.")
    
car1 = Car()
car1.go()