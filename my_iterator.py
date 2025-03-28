class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        raise StopIteration
    
    
for num in MyIterator(10):
    print(num)