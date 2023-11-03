try:
    file = open("file.txt", "r")
    print(file.read())
except:
    print("Error managing file")
finally:
    file.close()

with open("file.txt", "r") as file:
    print(file.read())


import time
from functools import wraps


def logger(functia_originala):
    @wraps(functia_originala)
    def wrapper(*args):
        result = functia_originala(*args)
        return result, args
    return wrapper


def timeit(functia_originala):
    @wraps(functia_originala)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = functia_originala(*args, **kwargs)
        t2 = time.time() - t1
        print(t2)
        return result
    return wrapper


@logger
def calculate(a, b):
    return a + b


print(calculate(2, 4))
