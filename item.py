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

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def get_price(self):
        return self.price

    def get_amount(self):
        return self.amount

    def get_perishable(self):
        return self.perishable

    def recieve_shipment(self, x):
        self.amount = self.amount + x
        return self.amount

    def sold(self, x):
        self.amount = self.amount - x
        return self.amount
