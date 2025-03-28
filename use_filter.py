from some_package.fib import fib_iter

for i in filter(lambda x: x % 2 == 0, fib_iter(10)):
    print(i)