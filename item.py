class Item():

    def __init__(self, id, name, cost, price, amount, perishable):
        self.id = id
        self.name = name
        self.cost = cost
        self.price = price
        self.amount = amount
        self.perishable = perishable

    def __str__(self):
        return "Item: {}, {}, {}, {}, {}, {}".format(self.id, self.name, self.cost, self.price, self.amount, self.perishable)

    def recieve_shipment(self, x):
        self.amount = self.amount + x
        return self.amount

    def sold(self, x):
        self.amount = self.amount - x
        return self.amount
