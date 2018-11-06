def multiples(n):
    """Find the sum of multiples of 3 and 5 for numbers below n."""
    result = []
    for i in range(0, n):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)
    return sum(result)


def test_multiples():
    assert multiples(10) == 23


if __name__ == '__main__':
    multiples(1000)