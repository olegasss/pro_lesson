# Task 1

class BalanceDescriptor:
    def __get__(self, instance, owner):
        return instance._balance

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Balance cannot be negative!")
        instance._balance = value

class Account:
    balance = BalanceDescriptor()

    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def __setattr__(self, name, value):
        if name == 'balance':
            if value < 0:
                raise ValueError("Balance cannot be negative!")
            self.__dict__['_balance'] = value
        else:
            super().__setattr__(name, value)

    def __getattr__(self, name):
        return f"Property '{name}' does not exist."

account = Account(100)
print(account.balance)

account.balance = 200
print(account.balance)

try:
    account.balance = -50
except ValueError as e:
    print(e)

print(account.some_property)



# Task 2

class User:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    def __setattr__(self, name, value):
        if name in ['first_name', 'last_name']:
            raise AttributeError(f"Changing '{name}' is not allowed.")
        super().__setattr__(name, value)

    def __getattr__(self, name):
        return f"Property '{name}' does not exist."

user = User("Oleg", "Glezin")

try:
    user.first_name = "Oleg"
except AttributeError as e:
    print(e)

print(user.middle_name)


# Task 3


import random

class Rectangle:
    def __init__(self, width, height):
        super().__setattr__('_width', width)
        super().__setattr__('_height', height)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        raise AttributeError("Cannot change 'width'")

    @height.setter
    def height(self, value):
        raise AttributeError("Cannot change 'height'")

    def __getattr__(self, name):
        return f"Property '{name}' does not exist"

    def area(self):
        return self._width * self._height

random_width = random.randint(3, 8)
random_height = random.randint(3, 8)
rect = Rectangle(random_width, random_height)

print(f"Width: {rect.width}, Height: {rect.height}")
print(f"Area: {rect.area()}")

try:
    rect.width = 15
except AttributeError as e:
    print(e)

try:
    rect.height = 20
except AttributeError as e:
    print(e)


print(rect.some_property)
