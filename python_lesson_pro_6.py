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

import logging

logging.basicConfig(level=logging.INFO)


def write_data_to_file(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            try:
                with open(file_name, 'a') as f:
                    f.write(f'{res}\n')
            except Exception as e:
                logging.error(e)
            return res
        return wrapper
    return decorator


@write_data_to_file('data.txt')
def my_func():
    return [1, 2, 3, 4]


print(my_func())


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


# Task 4

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Hour of execution '{func.__name__}': {execution_time:.10f} sec")
        return result
    return wrapper
@measure_time
def some_function():
    time.sleep(2)

some_function()


# Task 5

def log_arguments_results(func):
    def wrapper(*args, **kwargs):

        print(f"Arguments: {args}, Named arguments: {kwargs}")

        result = func(*args, **kwargs)

        print(f"Result: {result}")
        return result
    return wrapper

@log_arguments_results
def add_numbers(a, b):
    return a + b

add_numbers(3, 4)


# Task 6


def limit_calls(max_calls):
    def decorator(func):
        count = 0
        def wrapper(*args, **kwargs):
            nonlocal count
            if count < max_calls:
                count += 1
                return func(*args, **kwargs)
            else:
                print("Max call limit.")

        return wrapper

    return decorator
@limit_calls(3)
def some_function():
    print("Call function")

some_function()
some_function()
some_function()
some_function()


# Task 7

def cache_results(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@cache_results
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
print(fibonacci(10))
