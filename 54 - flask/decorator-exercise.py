import time


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        finish_time = time.time()
        duration = finish_time - start_time
        print(duration)
    return wrapper_function()


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i