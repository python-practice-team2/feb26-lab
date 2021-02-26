class Items():

    def __init__(name, cost, price, amount, perishable):
        self.name = name
        self.cost = cost
        self.price = price
        self.amount = amount
        self.perishable = perishable

    def __str__(self):
        return "Item: {}, {}, {}, {}, {}".format(self.name, self.cost, self.price, self.amount, self.perishable)

    def recieve_shipment(x):
        self.amount = self.amount + x
        return self.amount

    def sold(x):
        self.amount = self.amount - x
        return self.amount
