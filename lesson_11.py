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

