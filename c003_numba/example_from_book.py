import numba
from time import time
from math import sqrt
from functools import wraps

def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        ts = time()
        result = f()
        te = time()
        print(f"fun: {f.__name__}, args: [{args}, {kwargs}] took: {te-ts} sec")

        return result
    return wrap


@timing
@numba.jit(nopython=True)
def f():
    l = []
    for i in range(150000):
        l.insert(0, i)


f(200)  # 2.19 sec withut jit; and 0.29 sec with jit.