"""This function accepts two words and checks if one is an edit of the other."""

from collections import Counter


def oneaway(word1, word2):
    return True if len(Counter(word1) - Counter(word2)) == 1 else False


def test_one_edit():
    assert oneaway('pale', 'ple') == True
    assert oneaway('pales', 'pale') == True
    assert oneaway('pale', 'bale') == True


def test_not_one_edit():
    assert oneaway('pale', 'bake') == False
    assert oneaway('eat', 'drink') == False


if '__name__' == '__main__':
    oneaway()
