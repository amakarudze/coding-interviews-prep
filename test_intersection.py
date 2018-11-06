""""Check which characters are in both strings."""


def check_intersection(word1, word2):
    return set(word1) & set(word2)


def test_check_intersection():
    assert check_intersection('anna', 'mufaro') == {'a'}
    assert check_intersection('anna', 'shingi') == {'n'}
    assert check_intersection('anna', 'anastacia') == {'a', 'n'}


if '__name__' == '__main__':
    check_intersection()
