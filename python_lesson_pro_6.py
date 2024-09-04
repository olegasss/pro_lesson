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

import os
import json
from functools import wraps

def cache_results(filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            if not os.path.exists(filename):
                with open(filename, 'w') as f:
                    json.dump({}, f)

            with open(filename, 'r') as f:
                results = json.load(f)

            key = str(args)
            if key in results:
                print("Use of cached results.")
                return results[key]

            result = func(*args)
            results[key] = result
            with open(filename, 'w') as f:
                json.dump(results, f)

            return result
        return wrapper
    return decorator

@cache_results('results.json')
def add(a, b):
    return a + b

print(add(1, 2))
print(add(1, 2))


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
