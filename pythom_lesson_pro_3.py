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

class ProperFraction:
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if not isinstance(other, ProperFraction):
            other = ProperFraction(other)
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if not isinstance(other, ProperFraction):
            other = ProperFraction(other)
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __mul__(self, other):
        if not isinstance(other, ProperFraction):
            other = ProperFraction(other)
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if not isinstance(other, ProperFraction):
            other = ProperFraction(other)
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return ProperFraction(new_numerator, new_denominator)

    def __floordiv__(self, other):
        if not isinstance(other, ProperFraction):
            other = ProperFraction(other)
        new_numerator = self.numerator // other.numerator
        new_denominator = self.denominator // other.denominator
        return ProperFraction(new_numerator, new_denominator)


# Example
a = ProperFraction(5, 4)
b = ProperFraction(-1, 4)
c = ProperFraction(3, 8)
d = ProperFraction(3, 8)
e = ProperFraction(2, 3)

print(a)
print(b)
print(c)
print(d)
print(e)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)