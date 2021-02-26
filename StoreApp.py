from os import system
import math
from database import Database
from database import item

if __name__ == "__main__":
    item1 = item.Item(1, "Kitkat", 5, 2, 10, True)
    item2 = item.Item(2, "Coke", 3, 1, 10, True)

    store = Database()
    store.add_item(item1)
    store.add_item(item2)

    ls = store.get_item()


check=True
while(check):
    system("cls")
    print("------------------------------")
    print("1. Get price")
    print("2. See all items")
    print("3. Buy item")
    print("4. Exit")
    print("------------------------------")


    ch=int(input("Enter your choice: "))

    if ch == 1:
        for i in ls:
            print(str(i.name) + " : " + str(i.price) + "$")
    elif ch == 2:
        store.display_items()
    elif ch == 3:
        store.display_items()
        id = int(input("Which item? :"))
        store.buy_item(id)
    elif ch == 4:
        check=False
        print("Exiting...")
    else:
        print("Invalid Choice")
        pass

    input("\nEnter any key to continue...")


