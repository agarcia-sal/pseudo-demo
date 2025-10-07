from typing import List, Tuple

def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_m: str, char_n: str) -> str:
        # If chars are equal, return '0', else '1'
        if not (char_m != char_n):
            return '0'
        else:
            return '1'

    accumulator: str = ''
    pairs: List[Tuple[str, str]] = []
    for index in range(len(string_a)):
        pairs.append((string_a[index], string_b[index]))

    for first_char, second_char in pairs:
        accumulator += xor(first_char, second_char)

    return accumulator