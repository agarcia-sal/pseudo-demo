from typing import Iterator

def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_one: str, char_two: str) -> str:
        if not (char_one != char_two):
            return '0'
        return '1'

    output = []
    iterator_a: Iterator[str] = iter(string_a)
    iterator_b: Iterator[str] = iter(string_b)

    while True:
        try:
            c1 = next(iterator_a)
            c2 = next(iterator_b)
            output.append(xor(c1, c2))
        except StopIteration:
            break

    return ''.join(output)