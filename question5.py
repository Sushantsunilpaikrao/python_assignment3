class FibonacciIterator:
    def __init__(self, n_terms):
        self.n_terms = n_terms
        self.current = 0
        self.next = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n_terms:
            raise StopIteration
        self.count += 1
        fib = self.current
        self.current, self.next = self.next, self.current + self.next
        return fib

n_terms = 10
fib_iterator = FibonacciIterator(n_terms)
for num in fib_iterator:
    print(num)
