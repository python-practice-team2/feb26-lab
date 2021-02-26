import item
import math

class Database():

    items = []
    
    def add_item(self, new_item):
        self.items.append(new_item)

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
                item.sell_item

    def buy_items(self, id, amount):
        for item in self.items:
            if item.id == id:
                item.sell_items(amount)
    
    
if __name__ == "__main__":
    item1 = item.Item(1, "Kitkat", 5, 2, 10, True)
    item2 = item.Item(2, "Coke", 3, 1, 10, True)

    store = Database()
    store.add_item(item1)
    store.add_item(item2)

    print()
    store.display_items()
    store.perish()
    store.display_items()