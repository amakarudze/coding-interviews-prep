my_list = [ 104, 116, 116, 112, 115, 58, 47, 47, 101, 110, 103, 105, 110, 101, 101, 114, 105, 110, 103, 45, 97, 112, 112, 108, 105, 99, 97, 116, 105, 111, 110, 46, 98, 114, 105, 116, 101, 99, 111, 114, 101, 46, 99, 111, 109, 47, 113, 117, 105, 122, 47, 105, 112, 108, 115, 106, 102, 107, 102, 107, 114, 111, 100, 115, 101, 101, 103, 103 ]

chars = [chr(x) for x in my_list]

link = ''.join(chars)

print(link)