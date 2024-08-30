# Task 1

def sequence_generator(first_term, n, func):
    term = first_term
    for _ in range(n):
        yield term
        term = func(term)
def example_function(x):
    return x + 2
gen = sequence_generator(1, 5, example_function)
for value in gen:
    print(value)



# Task 2

def memoize(fn):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

import time

n = 30

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

start_time = time.time()
print("Fibonacci Recursive:", fibonacci_recursive(n))
print("Recursive time:", time.time() - start_time)


start_time = time.time()
print("Fibonacci Memoized:", fibonacci(n))
print("Memoized time:", time.time() - start_time)



# Task 3


def apply_function_and_sum(numbers, func):
    transformed_list = [func(x) for x in numbers]
    return sum(transformed_list)
if __name__ == "__main__":
    numbers = [1.1, 2, 3.5, 4.4, 8.3]
    def multiply_by_two(x):
        return x * 1
    result = apply_function_and_sum(numbers, multiply_by_two)
    print("Sum of the transformed list:", result)