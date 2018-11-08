"""Program that accepts two strings and check if one is a permutation of the other."""

from itertools import permutations


def perms(word):
    is_palindrome = False
    for w in permutations(word.lower()):
        if w == w[::-1]:
            is_palindrome = True
        else:
            is_palindrome = False
        print(w)
    return is_palindrome


def test_permutations():
    assert perms('anna') == True
    assert perms('Tact Coa') == False
    assert perms('hear') == False


if '__name__' == '__main__':
    perms()
