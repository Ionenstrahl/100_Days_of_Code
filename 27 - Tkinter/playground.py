def add(*args):
    result = 0
    for n in args:
        result += n
    return result

print(add(1,2,3))

def calculate(n, **kwargs):
    #for key, value in kwargs.items():
    #    print(key)
    #    print(value)
    n *= kwargs["multiply"]
    n += kwargs["add"]
    print(n)

print(calculate(2, add = 3, multiply = 4))

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make = "Nissan", model="GT-R")

