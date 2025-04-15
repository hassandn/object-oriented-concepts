class Animal:

    def __init__(self, name):
        self.name = name 
        
    
    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is sleeping!")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing!")


class predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting!")


class Rabit(Prey):
    pass


class Hawk(predator):
    pass

class Fish(predator , Prey):
    pass

rabit = Rabit("RabitMq")
fish = Fish("mfow")
hawk = Hawk("Hawk tuah")

rabit.flee()
hawk.hunt()
fish.hunt()
fish.flee()
fish.eat()