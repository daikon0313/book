class Customer:
    """顧客クラス"""

    def __init__(self, name, birthday, address):
        self.name = name
        self.birthday = birthday
        self.address = address

class Item:
    """商品クラス"""

    def __init__(self, name, price, purchase_price):
        self.name = name
        self.price = price
        self.purchase_price = purchase_price

    def cost_rate(self):
        return self.purchase_price / self.price
    
    def print_name(self):
        print(self.name)

item_1 = Item("りんご", 250, 100)
item_2 = Item("バナナ", 280, 200)
# print(f"原価率: {item_1.cost_rate()}")

item_1.print_name()
item_2.print_name()