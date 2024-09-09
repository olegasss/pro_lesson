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