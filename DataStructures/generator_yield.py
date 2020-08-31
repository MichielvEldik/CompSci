"""
A generator is a simple way to create an iterator.
Let's look at fibbonacci sequence.
"""


def fib():
    a, b = 0, 1  # initialize
    while True:
        yield a
        a, b = b, a + b


for f in fib():
    if f > 31:
        break
    print(f)
