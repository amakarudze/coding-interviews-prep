"""This function accepts two words and checks if one is an edit of the other."""

from collections import Counter


def one_away(word1, word2):
    return True if len(Counter(word1) - Counter(word2)) == 1 else False


if '__name__' == '__main__':
    one_away()
