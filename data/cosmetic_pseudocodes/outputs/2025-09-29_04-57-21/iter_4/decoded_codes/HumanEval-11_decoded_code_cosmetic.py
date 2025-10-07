from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(char1: str, char2: str) -> str:
        if not (char1 != char2):
            return '0'
        else:
            return '1'

    output = []
    index = 0
    length_a = len(string_a)
    length_b = len(string_b)
    while index < length_a and index < length_b:
        c1 = string_a[index]
        c2 = string_b[index]
        output.append(xor(c1, c2))
        index += 1
    return ''.join(output)