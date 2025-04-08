
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.

class Smartphone:
    def __init__(self, name, model, storage, price):
        self.name = name
        self.model = model
        self.storage = storage
        self.__price = price

    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price

    def display_smartphone_info(self):
        return (
            f"The name of the phone is: {self.name}\n"
             f"The model is: {self.model}\n" 
             f"The storage size is: {self.storage}GB\n"
             f"The price is: {self.__price}\n"
            )
    

class Tablet(Smartphone):
    def __init__(self, name, model, storage, price, screen_size):
        super().__init__(name, model, storage, price)
        self.screen_size = screen_size

    def display_tablet_properties(self):
        return (
            f"Your tablet is of name: {self.name}\n"
            f"The model is: {self.model}\n"
            f"The storage size is: {self.storage}\n"
            f"The price is: {self.get_price()}\n"
            f"The screen size is: {self.screen_size}\n"
        )

phone = Smartphone("Infinix HOT 30i", "Infinix X669B", 128, 15000)    
tablet = Tablet("Samsung X3", "Samsung", 512, 53000, "1080 * 612")

print(phone.display_smartphone_info())
print(tablet.display_tablet_properties())