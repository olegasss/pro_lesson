# Task 1

def my_decorator(func):
    def wrapper(*args, **kwargs):

        print("Initional")
        result = func(*args, **kwargs)
        print("Result processing")
        return result

    return wrapper
@my_decorator
def say_hello(name):
    print(f"My {name}!")
say_hello("Python")


# Task 2

















# Task 3

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
            return None
    return wrapper

@handle_exceptions
def divide(a, b):
    return a / b

result = divide(5, 0)
print(result)