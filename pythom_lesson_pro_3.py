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

class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product: Product, quantity: int):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_item(self, product: Product, quantity: int):
        if product in self.items:
            if self.items[product] <= quantity:
                del self.items[product]
            else:
                self.items[product] -= quantity

    def total_cost(self):
        total = 0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total

    def __iadd__(self, other: 'Cart'):
        for product, quantity in other.items.items():
            self.add_item(product, quantity)
        return self

if __name__ == "__main__":
    try:
        product = Product("Widget", 50.0)
        print(f"Product: {product.name}, Price: ${product.price:.2f}")

        product.set_price(-10.0)
    except InvalidPriceError as e:
        print(e)

    cart1 = Cart()
    cart1.add_item(Product("Product A", 10.0), 2)
    cart1.add_item(Product("Product B", 20.0), 1)

    cart2 = Cart()
    cart2.add_item(Product("Product C", 15.0), 3)
    cart2.add_item(Product("Product D", 25.0), 1)

    cart1 += cart2
    print(f"Total cost: ${cart1.total_cost():.2f}")


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


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} using PayPal.")


class SequenceProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} using Sequence Protocol.")


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

cart.set_payment_processor(SequenceProcessor())
cart.checkout()

#Task 3

import math

class RationalNumber:

    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int):
            raise TypeError("Numerator must be an integer")
        if not isinstance(denominator, int):
            raise TypeError("Denominator must be an integer")
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __ne__(self, other):
        return self.numerator * other.denominator != self.denominator * other.numerator

    def __lt__(self, other):
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __le__(self, other):
        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __gt__(self, other):
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __ge__(self, other):
        return self.numerator * other.denominator >= self.denominator * other.numerator

    def __radd__(self, other):
        return self.__add__(other)

    def __add__(self, other):
        if isinstance(other, int):
            other = RationalNumber(other, 1)

        if not isinstance(other, RationalNumber):
            return NotImplemented

        x = self.numerator * other.denominator + self.denominator * other.numerator
        y = self.denominator * other.denominator
        return RationalNumber(x, y)

    def __str__(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

        sign = '-' if self.numerator * self.denominator < 0 else ''
        tmp_x = abs(self.numerator)
        tmp_y = abs(self.denominator)

        if tmp_x == 0:
            return '0'

        if tmp_y == 1:
            return f'{sign}{tmp_x}'

        if tmp_x == tmp_y:
            return f'{sign}1'

        if tmp_x > tmp_y:
            return f'{sign}{tmp_x // tmp_y} {tmp_x % tmp_y}/{tmp_y}'

        return f'{sign}{tmp_x}/{tmp_y}'


x_1 = RationalNumber(1, 2)
x_2 = RationalNumber(3, 2)
x_3 = RationalNumber(1, -3)
x_4 = RationalNumber(-3, -1)
x_5 = RationalNumber(0, 1)

print(x_1, x_2, x_3, x_4, x_5, sep='\n')

y_1 = 2 + x_1
print(y_1)
