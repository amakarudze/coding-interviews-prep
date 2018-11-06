def get_earliest(first, second):
    """Return the earliest string date from two date strings."""
    (month1, day1, year1) = first.split('/')
    (month2, day2, year2) = second.split('/')
    if (month1, day1, year1) < (month2, day2, year2):
        return first
    else:
        return second


if __name__ == '__main__':
    get_earliest()
