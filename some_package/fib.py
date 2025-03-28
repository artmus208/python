
class fib_iter:
    def __init__(self, limit):
        self.i_prev = 0
        self.i = 1
        self.limit = limit
        self.count = 0
        
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.limit:
            self.current = self.i_prev
            self.i_prev, self.i = self.i, self.i_prev + self.i
            self.count += 1
            return self.current
        raise StopIteration
    
    def __repr__(self):
        return f"fib_iter(limit={self.limit!r})"
    
    def __str__(self):
        return f"Fibonacci numbers iterator with limit: {self.limit}"

# print(__name__)     # Имя модуля
# print(__file__)     # Путь к файлу
# print(__package__)  # Имя пакета
if __name__ == "__main__":
    f = fib_iter(100)
    for i in f:
        print(i)
        