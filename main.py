class item:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class shopping_cart:
    def __init__(self):
        self.items = []
        self.total_cost = 0

    def adding_item(self, add_item):
        self.items.append(add_item)
        self.total_cost += add_item.price

    def removing_item(self, remove_item):
        if remove_item in self.items:
            self.items.remove(remove_item)
            self.total_cost -= remove_item.price

    def clear_cart(self):
        self.items = []
        self.total_cost = 0

    def print_cart_info(self):
        for i in self.items:
            print(f"{i.name}: {i.price}")
        print(self.total_cost)


cart = shopping_cart()
milk = item("Milk", 2)
chips = item("Chips", 1)
broccoli = item("broccoli", 1)

for x in range(2):
    cart.adding_item(milk)

for x in range(3):
    cart.adding_item(broccoli)

for x in range(5):
    cart.adding_item(chips)

# cart.clear_cart()
for x in range(6):
    cart.removing_item(chips)

cart.print_cart_info()
