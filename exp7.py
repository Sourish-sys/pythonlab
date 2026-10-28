class Car:
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model
    def display(self):
        print("Car Brand:", self.brand)
        print("Car Color:", self.color)
        print("Car Model:", self.model)
car1 = Car("Toyota", "Black", "Fortuner")
car1.display()
