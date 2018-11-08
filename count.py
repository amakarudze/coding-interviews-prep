"""Count how many times a word is repeated in a sentence."""

import re
from collections import Counter


def count_words(string):
    """Return the number of times each word occurs in the string."""
    return Counter(re.findall(r"[\w'-]+", string.lower()))


if '__name__' == '__main__':
    count_words()
