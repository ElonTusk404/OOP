class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def description(self):
        print(self.brand)
        print(self.model)
        print(self.year)

    def is_old(self):
        if self.year < 2010:
            return True
        else:
            return False
car1 = Car("Toyota", "Camry", 2008)
car2 = Car("Honda", "Civic", 2015)
car3 = Car("BMW", "X5", 2020)
car1.description()
car2.description()
car3.description()
car1.is_old()
car2.is_old()
car3.is_old()