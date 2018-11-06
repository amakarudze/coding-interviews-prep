"""Program to check whether a word has all unique characters."""


def unique(word):
    characters = list(word.lower())
    character_count = {}
    is_unique = False
    for i in characters:
        character_count[i] = characters.count(i)
    for value in character_count.values():
        is_unique = False if value > 1 else True
    return is_unique


def test_unique():
    assert unique('Anna') == False
    assert unique('Genius') == True
    assert unique('bed') == True


if '__name__' == '__main__':
    unique()
