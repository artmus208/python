from some_package.fib import fib_iter

f = fib_iter(10)
print("from main.py", __file__)
for i in f:
    print(i)
    
print(f.__dict__)
    
def some_function(a: int, b: int) -> int:
    c = a + b
    return c

print(some_function.__annotations__)


print(f)
f_repr = eval(repr(f))
print(f_repr)