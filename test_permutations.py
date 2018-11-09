"""Program that accepts two strings and check if one is a permutation of the other."""

from itertools import permutations


def perms(word):
    is_palindrome = False
    for w in permutations(word.lower()):
        if ''.join(w).strip(' ') == ''.join(w[::-1]).strip(' '):
            is_palindrome = True
            break
        else:
            is_palindrome = False
    return is_palindrome


def test_permutations():
    assert perms('anna') == True
    assert perms('Tact Coa') == True
    assert perms('hear') == False


if '__name__' == '__main__':
    perms()
