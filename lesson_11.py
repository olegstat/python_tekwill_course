#1

def my_decorator(func):
    def wrapper():
        func()
        func()
        func()
    return wrapper

@my_decorator
def hello():
    print("hello")
hello()

#2

import time
def my_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        execution_time = end - start
        print(f"Execution time is: {execution_time}")
    return wrapper

@my_decorator
def sum_one_million():
    s = 0
    for i in range(1000000):
        s += i
    return s

sum_one_million()

#3

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        print(func(*args, **kwargs))
    return wrapper

#4

import time

def repeat(n, x):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
                time.sleep(x)
        return wrapper
    return decorator

@repeat(2, 1)
def f():
    print("hi")
f()

#5

def zero_division_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print("Division by 0 is not allowed")
    return wrapper


@zero_division_decorator
def divisor_function(number, divisor):
    return number / divisor
