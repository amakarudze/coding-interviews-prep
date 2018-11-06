"""Program that accepts two strings and check if one is a permutation of the other."""


def permutations(word1, word2):
    if set(word1) == set(word2):
        is_perm = True
    else:
        is_perm = False
    return is_perm


def test_permutations():
    assert permutations('pale', 'leap') == True
    assert permutations('data', 'tada') == True
    assert permutations('hear', 'here') == False


if '__name__' == '__main__':
    permutations()
