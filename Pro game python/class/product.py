class product:
    def __init__(self, id, name, description, price, quantity):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
    def display(self):
        print(self.id, self.name, self.description, self.price, self.quantity)

Product1 = product(1919191127, "fan", "used for cooling", "$68.99", 1)
Product2 = product(5373272356, "chair", "used for sitting on, luxery model", "$820", 6)
Product1.display()
Product2.display()