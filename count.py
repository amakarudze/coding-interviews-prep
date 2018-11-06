"""Count how many times a word is repeated in a sentence."""


def count_words(sentence):
    words = sentence.lower().split(" ")
    word_dict = {}
    for word in words:
        word_dict[word] = words.count(word)
    return word_dict


if '__name__' == '__main__':
    count_words()
