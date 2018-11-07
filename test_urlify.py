""""Replace whitespaces with '%20' in urls."""


def urlify(url):
    url = url.strip()
    url_2 = ''
    i = 0
    while i < len(url):
        if url[i] == ' ':
            url_2 = url_2 + '%20'
        else:
            url_2 = url_2 + url[i]
        i = i + 1
    url = url_2
    return url


def test_urlify():
    assert urlify("Mr John Smith   ") == "Mr%20John%20Smith"
    assert urlify("The Big Bang Theory Season 1") == "The%20Big%20Bang%20Theory%20Season%201"
    assert urlify("Friends") == "Friends"


if '__name__' == '__main__':
    urlify()
