class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"Product(name='{self.name}', price={self.price}, description='{self.description}')"
class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity=1):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def total_cost(self):
        total = sum(product.price * quantity for product, quantity in self.items.items())
        return total

    def __str__(self):
        cart_items = [(f"{product.name} (x{quantity}) - /n"
                       f"{product.price * quantity}") for product, quantity in self.items.items()]
        return "Cart:\n" + "\n".join(cart_items) + f"\nTotal cost: {self.total_cost()}"

if __name__ == "__main__":
    # Let's make a Mahito
    product1 = Product("Mint", 5.15, "Fresh mint leaves")
    product2 = Product("White Rum", 15.30, "A bottle of white rum")
    product3 = Product("Lemon", 3.50, "Fresh lemon")
    product4 = Product("Soda", 3.00, "Cold soda")
    product5 = Product("Ice", 2.15, "Cubed ice")

    cart = Cart()
    cart.add_product(product1, 1)
    cart.add_product(product2, 2)
    cart.add_product(product3, 1)
    cart.add_product(product4, 1)
    cart.add_product(product5, 1)

    print(cart)