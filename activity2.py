
# Create a program that includes animals or vehicles with the same action (like move()). 
# However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, 
# while Plane.move() prints "Flying" ✈️).

class Animal:
    def move(self):
        pass

class Bird(Animal):
    def move(self):
        return "Flying in the sky 🐦"  # Birds fly
    
class Fish(Animal):
    def move(self):
        return "Swimming in the water 🐟" # Birds swim
    
class Mammal(Animal):
    def move(self):
        return "Walking or running on land! 🐾"
    
animals = [Bird(), Fish(), Mammal()]

for animal in animals:
    print(f"{animal.__class__.__name__} is {animal.move()}")



