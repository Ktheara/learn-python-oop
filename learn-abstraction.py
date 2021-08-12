# Abstraction for hiding the internal details or implementations of a function and showing its functionalities only.
# The question is how do we use this abstraction exactly. The answer is by using inheritance.

from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    def description(self):
        print(f"This is {self.name} with {self.color}.")

    @abstractmethod
    def pricing(self):
        pass

class subCar(Car):
    def pricing(self):
        print(f"This price of this {self.name} is {self.price}")

#car1 = Car("Toyota", 3999, "Balck")
#car1.description()

car2 = subCar("Audi", 49933, "Red")
car2.pricing()