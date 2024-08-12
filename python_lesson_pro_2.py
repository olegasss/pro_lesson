#Task 1

from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float):
        """
        Process the payment. This method must be overridden in derived classes.
        """
        pass

class CreditCardProcessor(PaymentProcessor):
    def pay(self, amount: float):
        # Simulate processing a credit card payment
        print(f"Processing credit card payment of ${amount:.2f}")

class PayPalProcessor(PaymentProcessor):
    def pay(self, amount: float):
        # Simulate processing a PayPal payment
        print(f"Processing PayPal payment of ${amount:.2f}")

class BankTransferProcessor(PaymentProcessor):
    def pay(self, amount: float):
        # Simulate processing a bank transfer payment
        print(f"Processing bank transfer payment of ${amount:.2f}")

if __name__ == "__main__":
    amount_to_pay = 100.0

credit_card_processor = CreditCardProcessor()
paypal_processor = PayPalProcessor()
bank_transfer_processor = BankTransferProcessor()

credit_card_processor.pay(50.0)
paypal_processor.pay(75.0)
bank_transfer_processor.pay(100.0)


#Task 2

class Item:
    """
    Class representing an item in the cart.
    """

    def __init__(self, name, price):
        self.name = name
        self.price = price


class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError()


class CreditCardProcessor(PaymentProcessor):
    """
    Concrete implementation of a payment processor using credit cards.
    """

    def process_payment(self, amount):
        print(f"{amount}")
        # Here should be the logic for processing the payment with a credit card


class PayPalProcessor(PaymentProcessor):
    """
    Concrete implementation of a payment processor using PayPal.
    """

    def process_payment(self, amount):
        print(f"{amount}")
        # Here should be the logic for processing the payment with PayPal


class Cart:
    """
    Class representing the customer's shopping cart.
    Responsible for managing the items in the cart and processing payments.
    """

    def __init__(self):
        self.items = []
        self.payment_processor = None

    def add_item(self, item):
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
        """
        Processes the payment for the items in the cart using the set payment processor.
        """
        total = self.get_total()
        if self.payment_processor:
            self.payment_processor.process_payment(total)
            print()
        else:
            print()


cart = Cart()
cart.add_item(Item("Tea", 9.99))
cart.add_item(Item("Water", 3.90))

cart.set_payment_processor(CreditCardProcessor())
cart.checkout()

cart.set_payment_processor(PayPalProcessor())
cart.checkout()

#Task 3

class Discount:
    def apply(self, price):
        raise NotImplementedError
    """
    Discount is a base abstract class that defines a common interface for applying discounts.
    """

class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage
    def apply(self, price):
        return price * (1 - self.percentage / 100)
    """
    PercentageDiscount - A class that implements a discount as a percentage of the original price.
    """

class FixedAmountDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount
    def apply(self, price):
        return max(0, price - self.amount)
    """
    FixedAmountDiscount is a class that implements a discount as a fixed amount.
    """

original_price = 100
percentage_discount = PercentageDiscount(20)
print(f"Original price: {original_price}")
print(f"New price with 20% discount: {percentage_discount.apply(original_price)}")

fixed_amount_discount = FixedAmountDiscount(20)
print(f"New price with $20 discount: {fixed_amount_discount.apply(original_price)}")



#Task 4

class DiscountMixin:
    def apply_discount(self, discount):
        for item in self.cart:
            item.price = item.price * (1 - discount.rate)

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Discount:
    def __init__(self, rate):
        self.rate = rate

class Cart(DiscountMixin):
    def __init__(self):
        self.cart = []

    def add_item(self, item):
        self.cart.append(item)

    def total(self):
        return sum(item.price for item in self.cart)

# Example usage
item1 = Item("Product A", 110)
item2 = Item("Product B", 25)

cart = Cart()
cart.add_item(item1)
cart.add_item(item2)

discount = Discount(0.1)
cart.apply_discount(discount)

print(f"Total: {cart.total():.2f}")


