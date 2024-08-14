#Task 1

from abc import ABC, abstractmethod

class InvalidPriceError(ValueError):
    """InvalidPriceError, similar ValueError."""
    pass

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.set_price(price)

    def set_price(self, price: float):
        if price <= 0:
            raise InvalidPriceError("Price must be greater than 0")
        self.price = price

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float):
        """
        Process the payment. This method must be overridden in derived classes.
        """
        pass

class CreditCardProcessor(PaymentProcessor):
    def pay(self, amount: float):

        print(f"Processing credit card payment of ${amount:.2f}")

class PayPalProcessor(PaymentProcessor):
    def pay(self, amount: float):

        print(f"Processing PayPal payment of ${amount:.2f}")

class BankTransferProcessor(PaymentProcessor):
    def pay(self, amount: float):

        print(f"Processing bank transfer payment of ${amount:.2f}")

if __name__ == "__main__":
    try:
        product = Product("Widget", 50.0)
        print(f"Product: {product.name}, Price: ${product.price:.2f}")

        product.set_price(-10.0)
    except InvalidPriceError as e:
        print(e)


#Task 2

class InvalidQuantityError(Exception):
    pass
class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price

class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError()

class CreditCardProcessor(PaymentProcessor):

    def process_payment(self, amount):
        print(f"Processing payment of {amount} using Credit Card.")
        # Here should be the logic for processing the payment with a credit card

class PayPalProcessor(PaymentProcessor):

    def process_payment(self, amount):
        print(f"Processing payment of {amount} using PayPal.")
        # Here should be the logic for processing the payment with PayPal

class Cart:

    def __init__(self):
        self.items = []
        self.payment_processor = None

    def add_item(self, item):
        if item.price <= 0:
            raise InvalidQuantityError("Item price must be positive.")
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def set_payment_processor(self, processor):
        self.payment_processor = processor

    def checkout(self):

        total = self.get_total()
        if self.payment_processor:
            self.payment_processor.process_payment(total)
            print()
        else:
            print()

cart = Cart()
cart.add_item(Item("Tea", 9.99))
cart.add_item(Item("Water", 3.90))

try:
    cart.add_item(Item("Invalid Item", -5.00))
except InvalidQuantityError as e:
    print(f"Error: {e}")

cart.set_payment_processor(CreditCardProcessor())
cart.checkout()

cart.set_payment_processor(PayPalProcessor())
cart.checkout()

#Task 3

import logging

class LoggingMixin:
    """
    Mixin class that provides logging functionality.
    """
    def log(self, message):
        logging.basicConfig(filename='cart.log', level=logging.INFO, format='%(asctime)s - %(message)s')
        logging.info(message)

class Product(LoggingMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def change_price(self, new_price):
        self.price = new_price
        self.log(f"Price of '{self.name}' changed to {self.price}")

    def apply_discount(self, discount):
        discounted_price = self.price * (1 - discount)
        self.price = discounted_price
        self.log(f"Discount of {discount * 100}% applied to '{self.name}'. New price: {self.price}")

class Cart(LoggingMixin):
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)
        self.log(f"'{product.name}' added to the cart.")

    def remove_item(self, product):
        self.items.remove(product)
        self.log(f"'{product.name}' removed from the cart.")

    def get_total(self):
        total = sum(item.price for item in self.items)
        self.log(f"Total cart value: {total}")
        return total

product1 = Product("Tea", 5.0)
product2 = Product("Water", 2.0)

cart = Cart()
cart.add_item(product1)
cart.add_item(product2)

product1.change_price(30.0)
product2.apply_discount(0.2)

cart.remove_item(product1)
cart.get_total()



#Task 4

import logging

logging.basicConfig(
    filename='cart_events.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)class LoggingMixin:
    def log(self, message):
        logging.info(message)
class DiscountMixin(LoggingMixin):
    def apply_discount(self, discount):
        self.log(f"Applying {discount.rate * 100}% discount")
        for item in self.cart:
            original_price = item.price
            item.price = item.price * (1 - discount.rate)
            self.log(f"Changed price of {item.name} from {original_price:.2f} to {item.price:.2f}")


class Item(LoggingMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.log(f"Created new item: {self.name} - {self.price:.2f}")
class Discount:
    def __init__(self, rate):
        self.rate = rate
class Cart(DiscountMixin, LoggingMixin):
    def __init__(self):
        self.cart = []


    def add_item(self, item):
        self.cart.append(item)
        self.log(f"Added {item.name} to the cart")


    def total(self):
        return sum(item.price for item in self.cart)


    def pay(self):
        self.log(f"Total: {self.total():.2f}")
        self.log("Payment successful")


item1 = Item("Product A", 110)
item2 = Item("Product B", 25)

cart = Cart()
cart.add_item(item1)
cart.add_item(item2)

discount = Discount(0.1)
cart.apply_discount(discount)

cart.pay()


# Task 5

import logging


logging.basicConfig(filename='app_test.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Cart:
    def __init__(self):
        self.items = []
        self.discount = 0

    def add_item(self, product):
        if product.price <= 0:
            logging.error(f"Error '{product.name}' must be greater zero.")
            return
        self.items.append(product)
        logging.info(f"Product '{product.name}' added to the cart.")

    def apply_discount(self, discount):
        self.discount = discount
        logging.info(f"Discount of {self.discount * 100}% applied.")

    def total_cost(self):
        total = sum(item.price for item in self.items)
        return total * (1 - self.discount)

    def pay(self, payment_method):
        total = self.total_cost()
        logging.info(f"Paid with {payment_method}, amount: {total:.2f}")


def test_application():

    product1 = Product("Product 1", 10.99)
    product2 = Product("Product 2", -5.0)
    product3 = Product("Product 3", 15.50)


    cart = Cart()
    cart.add_item(product1)
    cart.add_item(product2)
    cart.add_item(product3)


    cart.apply_discount(0.1)
    cart.apply_discount(0.2)


    cart.pay("Cash")
    cart.pay("Credit card")

if __name__ == "__main__":
    test_application()