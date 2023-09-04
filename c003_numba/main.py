import numba
from time import time


@numba.jit(nopython=True)
def heavy_func():
    l = []
    for i in range(150000):
        l.insert(0, i)
    


if __name__ == "__main__":
    ts = time()
    heavy_func()
    te = time()
    print(f"fun: {__name__}, took: {te-ts} sec")