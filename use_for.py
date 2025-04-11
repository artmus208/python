
from my_decorator import timeit

@timeit
def classic_use_for_loop():
    l = list()
    for i in range(10**9):
        l.append(i)
    return l

@timeit
def list_comprehension():
    return [i for i in range(10**9)]


if __name__ == "__main__":
    classic_use_for_loop()
    list_comprehension()