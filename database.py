import item
import math

class Database():

    items = []
    
    def add_item(self, new_item):
        self.items.append(new_item)

    def get_item(self):
        return self.items

    def display_items(self):
        for item in self.items:
            print(item)

    def perish(self):
        for item in self.items:
            if item.perishable:
                item.amount -= int(math.floor(item.amount * .1))

    def buy_item(self, id):
        for item in self.items:
            if item.id == id:
                item.sold(1)

    def buy_items(self, id, amount):
        for item in self.items:
            if item.id == id:
                item.sell_items(amount)
    
