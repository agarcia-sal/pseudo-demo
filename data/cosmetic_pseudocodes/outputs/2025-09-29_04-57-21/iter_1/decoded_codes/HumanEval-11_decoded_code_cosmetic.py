from typing import Iterator

def string_xor(string_a: str, string_b: str) -> str:
    def xor(char1: str, char2: str) -> str:
        return '1' if char1 != char2 else '0'

    output = []
    for char1, char2 in zip(string_a, string_b):
        output.append(xor(char1, char2))
    return ''.join(output)