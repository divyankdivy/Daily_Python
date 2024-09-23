class CashRegister:

    TAX_RATE = 0.05

    def __init__(self, cashier):
        self.cashier = cashier
        self.products = {}

    def add_products(self, new_product, quantity=1):
        self.products[new_product["name"]] = {
            "price": new_product["price"],
            "quantity": quantity
        }

    def show_products(self):
        if self.products == {}:
            print("no products")
        else:
            for product in self.products:
                print(product)

    def remove_product(self, product):
        if product in self.products:
            del self.products[product]

    def update_price(self, product, price):
        if product in self.products:
            self.products[product]["price"] = price

    def subtotal(self):
        total = 0
        for product in self.products:
            total += self.products[product]["price"] * self.products[product]["quantity"]
        return total

    def show_subtotal(self):
        print(self.subtotal())

    def tax(self):
        tax_amount = self.subtotal() * CashRegister.TAX_RATE
        return tax_amount

    def show_tax(self):
        print(round(self.tax(), 2))

    def total_amount(self):
        total_after_tax = self.subtotal() + self.tax()
        return total_after_tax

    def show_total_amount(self):
        print(round(self.total_amount(), 2))

    def clear_products(self):
        self.products.clear()


macd = {"name": "Burger", 'price': 5.99}
domino = {"name": "Pizza", "price": 8.99}
kfc = {"name": "Chicken", "price": 12.99}

divy = CashRegister("Divyy")

divy.add_products(macd)
divy.add_products(domino)
divy.add_products(kfc)

divy.show_products()

divy.show_subtotal()
divy.show_tax()
divy.show_total_amount()
divy.update_price("Burger", 6.99)

divy.remove_product("Chicken")
divy.show_products()
divy.show_subtotal()
divy.show_tax()
divy.show_total_amount()

divy.clear_products()
divy.show_products()


