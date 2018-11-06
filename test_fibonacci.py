# Fibonacci series up to n and calculate the sum of even terms.
def fib(n):
    """Create a list of Fibonacci series up to n."""
    result = []
    even_terms = []
    a, b = 1, 2
    while a < n:
        result.append(a)
        if a % 2 == 0:
            even_terms.append(a)
        a, b = b, a+b
    return sum(even_terms)


def test_fib():
    assert fib(100) == 44


if __name__ == '__main__':
    fib(4000000)
